October 18th, 2016
======================

> John Hammond | Intro to Linux 2016

--------------------------------------

Recap:
-----

Welcome back to __Intro to Linux!__

Last week, you learned in [Training Wheels] how to interact with the _root_ user and even create and manage user accounts on your own. 

If you don't remember, does the command `sudo` ring a bell? It is "Super User Do"! ... in that you can temporarily _borrow_ the _root_ users powers to escalate your privileges and do things like install new software, add new users, or manage essential parts of the file system.

For Today's Class...
-------

Today, we'll be brushing the dust off of the `sudo` command and just briefly reviewing how to add a user. Then, we'll explore some simple networking things that [Linux] can do for us, an awesome thing called [`SSH`][SSH], and some file permissions. 

Let's dive right in!
-------

To get started, let's set the stage: today, you're going to be _remote controlling_ your friend's [Raspberry Pi]. That's right -- you're going to log into their computer... _from your computer!_

This works both ways, though -- just as you will be logging into their computer, _they_ will be logging into yours!

To set this up and to review some concepts from last week, we'll add a user to our machine.

Adding the User
----------------

You may not remember from last week, but last week we used a command called [`useradd`][useradd] to create a new user on your [Linux] computer. It wasn't very nice to us; we have to supply arguments for the user's home directory, their shell, we had to set the password separately, and other silly stuff.

I briefly mentioned at the end of the [Training Wheels] lesson that there is a better command to add a user, that simply has its words reordered: [`adduser`][adduser]. This will prompt you for the password and set everything up for you.

Let's create a user with an easy name like `linux` and a simple password like `is for penguins`. (I like to use spaces in my passwords [because it really amps up the entropy bits](http://lifehacker.com/5796816/why-multiword-phrases-make-more-secure-passwords-than-incomprehensible-gibberish) and the strength of the password) You don't have to use these exact credentials; but make it something simple and easy to remember, because you'll be telling them to your friend.

```
adduser linux
```


Oh! If you run this, you may get an error: `adduser: Only root may add a user or group to the system.`. Remember you need `sudo`!

```
sudo adduser linux
```

You should then be greeted with a lot of prompts, which you can fill out (or not fill out) however you would like, it really doesn't matter for the point of our exercise.

```
Adding user `linux' ...
Adding new group `linux' (1002) ...
Adding new user `linux' (1003) with group `linux' ...
Creating home directory `/home/linux' ...
Copying files from `/etc/skel' ...
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
Changing the user information for linux
Enter the new value, or press ENTER for the default
    Full Name []: Linux  
    Room Number []:  
    Work Phone []: 
    Home Phone []: 
    Other []: 
Is the information correct? [Y/n] y
```

Once you get your prompt back, you can do things to verify that the new user has been created. Try checking out the home directories with a command like `ls /home`, or even viewing the `/etc/passwd` file with `cat`. At this point, I trust you to be able to do things like that (if you feel unsure about them, let me know!)

Just for good measure, let's try and run a command as that new `linux` user with the `sudo` command. Remember how you can pass another username as an argument, and you can run commands as that user?

```
sudo linux whoami
```

You should see `linux` as your output. Hurray!

Next: Finding your Address
-----------

Now that you have the user set up for your friend to log in as, you will need to determine _your own [IP address]_ so they know where to try to and connect to.

You can find your [IP address] on [Linux] with the command: 

```
ifconfig
```

This shows you the _configuration_ for each _interface_ currently active on your [Linux] box. Typically, the wired connection is represent by `eth0`, denoting that it is with an _eth_ernet cable (and the computer is zero-based).

You should find your [IP address] similar to the form of `10.6.1.20` or something of the like. Again, this is information you want to keep track of so you can tell your friends. This is the address they will use to connect to your computer!

Starting to SSH!
--------

__Enter [`SSH`][SSH], the [Secure Shell][SSH]!__

[`SSH`][SSH] is a very commonly used utility in the world of [Linux]. You can think of it as a remote control connection from one computer to another; you can log in and interact with the box through the [command-line], the same way you do on your own machine. All the communication and networking over the [`SSH`][SSH] protocol is encrypted (hence the name "secure").

If you are curious, take a look at the description in the `man` page of the [`ssh`][ssh] command.

```
man ssh
```


When you and your friend are ready, exchange [IP addresses][IP address] and credentials. 

You will supply the "hostname" (in this case the [IP address]) that you want to connect to as an argument to [`ssh`][ssh].

```
ssh YOUR.FRIENDS.IP.ADDRESS
```

If you are asked about some `ECDSA` key, you can hit `yes`:

```
The authenticity of host '10.6.1.9 (10.6.1.9)' can't be established.
ECDSA key fingerprint is SHA256:3LyX9qgjdyrmUY39m8iiO6fsXhwakoNqAEVqFiQP71g.
Are you sure you want to continue connecting (yes/no)? yes
```


It should then prompt you for a password (I'm using `10.6.1.9` as an example):

```
pi@10.6.1.9's password:
```

Oh! ___Be careful!___

See how it is asking us for the `pi` user's password? That's not what we want... _we want to use the `linux` user!_ (Or whatever username your friend set up for you).

By default, [`ssh`][ssh] will use thee username of YOUR user, the currently logged in user when connecting to another host. To get around this, we can specify the username we want to connect with just like an e-mail address. Break out of the current prompt with `Control+C` and change your command to supply a username, like this:

```
ssh linux@YOUR.FRIENDS.IP.ADDRESS
```


Now you should be prompted for the correct password, which you can enter -- and you should be able to log in!

Explore!
--------------

You're in a whole new computer now. Explore! See if you can find your friends personal repository or their journal reflections. 

To drive a point home, try using the `ifconfig` to see your [IP address]. You should see your friend's [IP address], since that is the box you are currently on!

Remember that you can use commands like `w` and `who` to see active users on the computer you are using. This time, you should be able to see your connection in a "FROM" column. With the `who` command, you can even supply a `--ips` argument to see YOUR source IP address.

```
who --ips
```

Check out their home directory
---------

If you aren't already there, check out the home directory of the `pi` user on your friends box. Instead of running `ls` just regularly, pass a `-l` argument to it this time, to list more information.

```
ls -l
```

```
drwxr-xr-x 5 pi pi 4096 Sep 13 13:00 Desktop
drwxr-xr-x 8 pi pi 4096 Sep 13 12:38 linux_16
```

This should give you some different output than what you are used to `ls` giving you usually. This time, it includes more information about the __file permissions__ of the files you see.

The far left column has a bunch of random letters, right? That is actually a representation of the bits set on the file, as to whether or not the file is __readable__, __writable__, or __executable__.

There are 10 characters given:

* The first character, `d` or `-`, denotes whether or not the item on the same line is a directory or a regular file.
* The next three characters refer to the file permissions ___for the owner of the file___. The characters are seen as either `r`, `w`, or `x`, or a `-` if the bit is not set. The letters that are displayed means the the __FILE OWNER__ can do these things with the file.
* The next set of three characters refer to permissions `r`, `w`, or `x` again, but this time ___for the USER GROUP of the file___. 
* The final set of three characters refer to permissions `r`, `w`, or `x` once more, but this time ___for EVERYONE___. 

You can also see on the same line that there is `pi` visible. The first occurence is the _user group_ that the file is a part of (it just happens to have the same name as the user). The next occurence of `pi` is telling you that the ___OWNER___ of this file is the `pi` user.

Well, since we are not the `pi` user and we are currently the `linux` user, the file permissions in the first set (the first triplet of `r`, `w`, and `x`) do not apply to us. We are only concerned with the _last_ three characters, and whether or not those file permissions are set for us.

We can see `r-x`, in the last bit, meaning that for __all users__ they can read and execute, but they cannot write. That makes sense, right? We shouldn't be able to tamper with our friends stuff.

Try it!
----------

If you want, fire up `nano` and see if you can save any files. It should give you a `Permission denied`. Even try to do some redirection with `echo`:

```
echo "Please work" > my_file.txt
-bash: my_file.txt: Permission denied
```

Dang! How have we gotten around the `Permission denied` error before? Well, we brought out the big guns... we tried to become _root_, the administrator of the whole computer.

Let's try that now. Just use a simple command and try to run it as _root_.

```
sudo ls
```

```
linux is not in the sudoers file.  This incident will be reported.
```

We can't become _root_! Apparently our `linux` user is not in the `sudoers` file, which is another special file in [Linux] that determines what users can use the `sudo` command. 

Well, what can we do, then?
-------

We are on our friends box, and we want to get cozy.

Since we have this `linux` user dedicated to us right now, we can use its home directory however we want. If you navigate to the `/home` directory and check out the file permissions with `ls -l` again, you should be able to see you are the owner of your own home directory (duh)!

```
drwxr-xr-x  2 gcwyman gcwyman 4096 Sep  1  2015 gcwyman
drwxr-xr-x  2 linux   linux   4096 Oct 18 02:58 linux
drwxr-xr-x 21 pi      pi      4096 Sep 20 12:33 pi
```

And don't forget! The `/tmp` directory is ___WORLD-READABLE___ and ___WORLD-WRITABLE___. Check it out:

```
ls -l /
```

```
total 88
drwxr-xr-x   2 root root  4096 Aug 21  2015 bin
drwxr-xr-x   3 root root 16384 Jan  1  1970 boot
drwxr-xr-x  12 root root  3220 Sep 20 12:55 dev
drwxr-xr-x 114 root root  4096 Oct 18 03:21 etc
drwxr-xr-x   5 root root  4096 Oct 18 02:58 home
drwxr-xr-x  15 root root  4096 Aug 21  2015 lib
drwx------   2 root root 16384 May  6  2015 lost+found
drwxr-xr-x   2 root root  4096 May  6  2015 media
drwxr-xr-x   2 root root  4096 Jan 11  2015 mnt
drwxr-xr-x   6 root root  4096 May  6  2015 opt
dr-xr-xr-x  75 root root     0 Jan  1  1970 proc
drwx------   2 root root  4096 May  6  2015 root
drwxr-xr-x  15 root root   600 Sep 20 12:55 run
drwxr-xr-x   2 root root  4096 Aug 21  2015 sbin
drwxr-xr-x   2 root root  4096 Jun 20  2012 selinux
drwxr-xr-x   2 root root  4096 May  6  2015 srv
dr-xr-xr-x  11 root root     0 Jan  1  1970 sys
drwxrwxrwt   4 root root  4096 Oct 18 03:17 tmp
drwxr-xr-x  10 root root  4096 May  6  2015 usr
drwxr-xr-x  11 root root  4096 May  6  2015 var
```

If you see the line for the `/tmp` directory, you'll notice it has all bits for file permissions set. 

```
drwxrwxrwt   4 root root  4096 Oct 18 03:17 tmp
```

But, the `root` user owns it?? You can see `root` is the name given as the user...

_Oh well!_ Since the last triplet for `r`, `w`, and `x` are set, __EVERYONE__ has read, write, and execute permissions. 

You can always make a home for yourself in the `/tmp` folder. You can make a directory with `mkdir`, cook up some files with `nano`, and do whatever you'd like. 

Keep poking around!
-----

That is just about all I wanted to show you for todays class. Super simple, I know -- but the real fun comes from you continuing to hunt around your friends computer and seeing what you have access to. What can you change? What commands can you run, what can't you run? How does that `/etc/passwd` file look?

When you are finished and want to disconnect from the [`ssh`][ssh] connection, you can enter `exit` to get back to your own machine. At that point you can [`ssh`][ssh] again at any point.

If you want, have some fun with this. How many people can you [`ssh`][ssh] into? Can you get everyone in the class to [`ssh`][ssh] into your computer, and try and wreak havoc?

When you are connected to the other computer, can you do any damage even without having `root` access? ___Have you ever heard of a [fork bomb]??___

You should change your passwords!
=================

Once you and your friends are all done trying to delete each others files, 
be cognizant of the fact that you just shared your [IP address].

If you are all done with today's exercise, remember to remove your extra user with the `deluser` command.

Also.... Do you remember when you started to [`SSH`][SSH] as the regular `pi` user? Does that user still have the default password? ___Is there anyone left in the room who has not yet changed that password?___

Remember you can change the password of a user with the `passwd` command.


[Training Wheels]: https://github.com/macee/linux_16/tree/master/training_wheels
[MicroSD]: https://en.wikipedia.org/wiki/MicroSD
[Raspbian]: https://www.raspberrypi.org/downloads/raspbian/
[operating system]: https://en.wikipedia.org/wiki/Operating_system
[operating systems]: https://en.wikipedia.org/wiki/Operating_system
[github]: https://github.com/
[bash]: https://en.wikipedia.org/wiki/Bash_(Unix_shell)
[IMG]: https://en.wikipedia.org/wiki/IMG_(file_format)
[Linux]: https://en.wikipedia.org/wiki/Linux
[Microsoft Windows]: https://en.wikipedia.org/wiki/Microsoft_Windows
[command-line]: https://en.wikipedia.org/wiki/Command-line_interface
[command line]: https://en.wikipedia.org/wiki/Command-line_interface
[Raspberry Pi]: https://www.raspberrypi.org/
[open-source]: https://en.wikipedia.org/wiki/Open-source_software
[Python]: https://www.python.org/
[github]: https://github.com
[Flask]: http://flask.pocoo.org/
[JSON]: http://www.json.org/
[SSH]: https://en.wikipedia.org/wiki/Secure_Shell
[useradd]: https://linux.die.net/man/8/useradd
[adduser]: http://askubuntu.com/questions/345974/what-is-the-difference-between-adduser-and-useradd
[IP Address]: https://en.wikipedia.org/wiki/IP_address
[fork bomb]: https://en.wikipedia.org/wiki/Fork_bomb