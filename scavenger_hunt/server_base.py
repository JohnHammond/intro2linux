#!/usr/bin/env python

from flask import Flask
from flask import render_template, request, session, g, url_for, flash, get_flashed_messages, redirect
import sqlite3
import json
import sys, os
from colorama import *
import sys

from passlib.hash import sha256_crypt
from contextlib import closing

debug = True
init( autoreset = True )

if (debug):

	def success( string ):
		print Fore.GREEN + Style.BRIGHT + "[+] " + string

	def error( string ):
		sys.stderr.write( Fore.RED + Style.BRIGHT + "[-] " + string + "\n" )

	def warning( string ):
		print Fore.YELLOW + "[!] " + string

else:
	def success( string ): pass
	def error( string ): pass
	def warning( string ): pass

# ============================================================

DATABASE = '$DATABASE'
CONFIG = '$CONFIGURATION'
CERTIFICATE = '$CERTIFICATE_FILE'
PRIVATE_KEY = '$PRIVATEKEY_FILE'

SECRET_KEY = 'this_key_needs_to_be_used_for_session_variables'

if DATABASE == '$DATABASE':
	error("This server has not yet been configured with a database file!")
	exit(-1)

if CONFIG == '$CONFIGURATION':
	error("This server has not yet been configured with a configuration file!")
	exit(-1)

if CERTIFICATE == '$CERTIFICATE_FILE':
	error("This server has not yet been configured with a certificate!")
	exit(-1)

if PRIVATE_KEY == '$PRIVATEKEY_FILE':
	error("This server has not yet been configured with a private key!")
	exit(-1)

app = Flask( __name__ )

app.config.from_object(__name__)

needed_configurations = [
	"app_title", "app_about", "app_navigation_logged_out",
	"app_navigation_logged_in", "challenges"
]

if not ( os.path.exists(CONFIG) ):
	error("This configuration file '" + CONFIG + "' does not seem to exist!")
	exit(-1)
else:
	success("The configuration file exists!")
	handle = open( CONFIG )
	configuration = json.loads(handle.read().replace("\n","").replace("\t",""))
	try:
		for needed_config in needed_configurations:
			assert configuration[needed_config]
	except Exception as e:	
		error("Configuration file '" + sys.argv[1] + "' does not have the following configuration tag:")
		warning(e.message)
		error("Please fix this and re-run the server.")
		exit(-1)
	
	handle.close()

	success("The configuration looks good!")
	success("Spinning up the server...")
	
def init_db():
	with closing(connect_db()) as db:
	    with app.open_resource(app.config['DATABASE'], mode='r') as f:
	        db.cursor().executescript(f.read())
	    db.commit()

def connect_db():
	return sqlite3.connect( app.config['DATABASE'] )

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def render( template_name, **kwargs ):
	return render_template( template_name, 
							app_title = configuration['app_title'], 
							app_navigation_logged_out = configuration['app_navigation_logged_out'],
							app_navigation_logged_in = configuration['app_navigation_logged_in'],
							**kwargs
						   )

@app.route("/login", methods=["GET", "POST"])
def login():

	error = ""
	if request.method == "POST":

		cur = g.db.execute('select username, password from users')
		# username, password_hash
		users = dict(( row[0], row[1] ) for row in cur.fetchall())

		if not request.form['username'] in users.iterkeys():
			error = 'This username is not in the database!'
		else:

			if not ( sha256_crypt.verify( request.form['password'], users[request.form['username']] ) ):
				error = "Incorrect password!"
			else:
				
				session_login( request.form['username'] )

				return redirect( "challenges" )

	return render( 'login.html', error = error )


@app.route("/register", methods=["GET", "POST"])
def register():

	cur = g.db.execute('select username from users')
	
	usernames = [row[0] for row in cur.fetchall() ]

	error = ""
	if request.method == "POST":

		if unicode(request.form['username']) in usernames:
			error = 'This username is already in use!'
		elif (request.form['password'] == ""):
			error = "You must supply a password!"
		elif request.form['password'] != request.form['confirm']:
			error = 'Your passwords do not match!'
		else:

			cur = g.db.execute('insert into users (username, password, solved_challenges, score, last_submission) values ( ?, ?, ?, ?, ? )', [ 
				               request.form['username'], 
				               sha256_crypt.encrypt( request.form['password']),
				               "",  # No challenges completed
				               0,   # no score.
				               0,   # and no last submission time.
				  ] )

			g.db.commit()


			flash("Hello " + request.form['username'] + ", you have successfully registered!")
			session_login( request.form['username'] )
			return redirect( "challenges" )

	return render( 'register.html', error = error )


@app.route("/scoreboard")
def scoreboard(): 

	cur = g.db.execute('select username, score from users order by score desc, last_submission asc')	
	response = cur.fetchall()	
	
	users = [ { "username": row[0], "score": row[1] } for row in response]
	
	return render("scoreboard.html", users = users )

@app.route("/logout")
def logout():

	session_logout()
	return redirect("about")

@app.route("/")
@app.route("/about")
def about(): return render("about.html", app_about=configuration['app_about'])

@app.route("/challenges")
def challenges_page(): 
	if not ( session['logged_in'] ):
		return render("login.html", error = "You must log in to be able to see the challenges!")	
	return render("challenges.html", challenges = configuration['challenges'])

@app.route("/check_answer", methods=["GET", "POST"])
def check_answer(): 

	if request.method == "POST":
		if request.form['challenge_id'] in session['solved_challenges'].split():

			return json.dumps({'correct': -1});

		correct_answers = configuration['challenges'][int(request.form['challenge_id'])]["possible_answers"]

		if ( request.form['answer'] in correct_answers ):

			new_solved_challenges = session['solved_challenges'] + " " +request.form['challenge_id']
			new_score = int(session['score']) + configuration['challenges'][int(request.form['challenge_id'])]["points"]
			cur = g.db.execute("update users set solved_challenges = (?), score = (?), last_submission = (SELECT strftime('%s')) where username = (?)", [
					new_solved_challenges,
					new_score, 
					session['username']
				] );

			session['score'] = new_score
			session['solved_challenges'] = new_solved_challenges
			g.db.commit();

			return json.dumps({'correct': 1, 'new_score': new_score});
		else:
			return json.dumps({'correct': 0});

def session_login( username ):
	
	flash("You were successfully logged in!")

	cur = g.db.execute('select solved_challenges, score from users where username = (?)',
			[username])	

	solved_challenges, score = cur.fetchone()

	session['logged_in'] = True
	session['username'] = username
	session['solved_challenges'], session['score'] = solved_challenges, score

def session_logout():

	flash("You have been  successfully logged out.")

	session['logged_in'] = False
	session.pop('username')
	session.pop('score')

def prepare_challenges():

	for i in range(len( configuration['challenges'])):
		challenge = configuration['challenges'][i]
		challenge["id"] = str(i)
 
if ( __name__ == "__main__" ):

	prepare_challenges()
	context = (CERTIFICATE, PRIVATE_KEY)
	app.run( host="0.0.0.0", debug=False, ssl_context=context, port = 2000, threaded = True )
	#app.run( host="0.0.0.0", debug=False, port = 2000, threaded = True )

