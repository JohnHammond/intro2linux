Class for November 29th
===========================

> John Hammond | Nov 29th, 2016

-------------------------

Working with MySQL
================

You can interact with a SQL database in a much better and much more efficient way, compared to what you are probably used to when working with languages like C#, or trying to play-pretend with an Access database or Excel spreadsheet.

On Linux, we can connect to a MySQL database in _pure text_, and send it raw, vanilla SQL statements. It's an interpreter and a shell, just like `bash` or Python: so you will see your results right away.

Installing MySQL Server and Client
----------

To install MySQL, please run

``` bash
sudo apt install mysql-server
```

When it installs it should prompt you for a "root" password. __Note that this is not the root password for your Linux machine!__ It is instead a user for the MySQL server and database to use on its own.

Connecting to the Server
--------------

Once it has finished installing, you can try to run `mysql`

Notice that it will give you an error, saying you cannot connect with that username. If you read the man page for the MySQL command you can find other options, but you should know that `-u` and an argument can help specify the username. We will have to specify the `root` user, since that is currently the only one that MySQL has to work with.

When you that command, `mysql -u root` it still does not let you connect! Why is that? You need to specify `-p` to say that will enter a password. Then, you will be prompted to enter the password you created when you installed MySQL.

Once you are connected to the MySQL server, you will be given a nice prompt:

```
mysql>
```

The banner explains that you can run `help;` to see other commands. If you want, go ahead and run that:

``` sql
help;
```

Using Databases
----------------

Okay, well, now that we are connected to the MySQL server, what do we do?

It will cool to be able to create and work with databases, right? So first, we should see what is available to us.

At your prompt, you can see what databases the MySQL server has with the command:

``` sql
SHOW DATABASES;
```


__Notice you needed to type a semi-colon `;`! These are _mandatory_ in MySQL.__ If you do not type a semi-colon, and leave your line empty, like just `SHOW DATABASES`, you will see another prompt, and no matter what you do, it will not seem to go away! Even `Control+C` won't break you out of it. You will have to supply a semi-colon `;` for MySQL to understand that you want this command to end.


So when you do run `SHOW DATABASES;`, you should be given a list of what databases the MySQL server has:

``` 
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.01 sec)
```


Since we _just_ installed the MySQL server, there is really nothing here other than the internals for MySQL. Those won't really help us in storing any data for ourselves, because they are already filled with data. The `sys` databases stores things like MySQL session variables and environment variables and user accounts, and the `information_schema` database actually stores information _about other databases_, all the ones that you create on your own. Since those are all "under-the-hood" for MySQL, they are very handy for hacking.

But, we want a database for ourselves! So, let's create one.

``` sql
CREATE DATABASE uscga;
```

And you should see...

```
Query OK, 1 row affected (0.00 sec)
```


Now if you run `SHOW DATABASES;`, you should see your entry!

We're not done yet. If we actually want to interact with that database, we have to tell MySQL that we want to _use_ that database.

``` sql
USE uscga;
```

And it should tell you `Database changed`. Sweet, now we're in business!


Working with Tables
--------------------

Now, we need the next container down: what tables are in the database? 

We can use the same kind of query to see the tables, like we did the databases. We can use:

``` sql
SHOW TABLES;
```

Right now, it should tell you 

``` 
Empty set (0.00 sec)
```

We don't have any tables yet! Let's create some.

Since every table has to have columns, and those columns have to have special data types, we have to specify those when we are creating our table.

There are lots of data types, all like what you already know and are used to -- we just have to know the syntax and what they are really called in MySQL. There are some like `int`, `date`, `decimal`, and more. You can find them all online. You should know, however, that we have to explicitly declare maximum lengths or sizes for strings. MySQL calls them `varchar`s, and we will specify the length like so:

``` sql
CREATE TABLE cadets ( cadet_code int, first_name varchar(20), last_name varchar(20) );
```

Now you should be able to `SHOW TABLES;` and see your new one!

Since we set up those columns, we can see more information about them with this syntax:

``` sql
SHOW COLUMNS FROM cadets;
```


The are of course other things you can set up, like what fields should auto increment or which is the primary key (etc.) but if you need to use them, you ought to look them up on your own.

Interacting with Data
---------------

Inserting data should be easy for you; I'm sure you have done this many times before, just with wrappers in other languages, like C# or otherwise. 

From this point on you should be able to run commands like you have seen before:

```  sql
INSERT INTO cadets VALUES ( 18336, "John", "Hammond" );
```

``` sql
UPDATE cadets SET first_name = "Full", last_name = "Rack" WHERE cadet_code = "18336";
```

``` sql
SELECT last_name FROM cadets WHERE cadet_code = "18336";
```


Cleaning up
============

Deleting a table
----------

If you ever want to delete a database for some reason, you can use the syntax:

``` sql
DROP TABLE <table_name>;
```

Deleting a database
----------

If you ever want to delete a database for some reason, you can use the syntax:

``` sql
DROP DATABASE <db_name>;
```

__Your user must have the super-delete privilege to be able to do this.__