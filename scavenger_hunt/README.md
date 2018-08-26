Linux Scavenger Hunt
========================

<p align="center">
  <img src="https://github.com/macee/linux_16/blob/master/pictures/bash.png?raw=true" alt="The bash shell"/>
</p>

The "[Linux] Scavenger Hunt" is a [CTF]-like activity to encourage the student to work on their own to explore the [Linux] filesystem, navigating in and out of directories to find different files. 

---------

The Server
----

To prepare the server, you should run the [`bash`][bash] script with arguments to supply a path for the [sqlite3] database it will create and use, and supply the [JSON] file that includes the challenges and flags. So an example setup would look like:

```
sudo ./setup.sh -d /tmp/database.db -c scavenger.json
```

Once the server has installed all the dependencies and set up the system, you can run the server with:

```
sudo python server.py
```

The server runs threaded, and typically tries to use a certificate to work with an [HTTPS] connection (so no one could try and listen for flags and passed aren't passed in the clear), but lately this has been giving me trouble.

If you would like to reconfigure how the server sets itself up (port number, use of [HTTPS], etc..), then modify the last line of the `server_base.py` file (which the `setup.sh` uses to build off of).


---------------


The Client (End-User)
------------------

The client (the student, in this case) should have access to the repository but they should just run the initial `scavenger_hunt` file to set up the game. This is a simple [`bash`][bash] script that creates all the `FINDME.txt` files with the flags to submit (they are in plain text, but I don't expect any student to try and cheat and look at the flags in the script).

They should then be able to navigate to the web server and start to submit the flags, playing the Linux Scavenger Hunt!


Files & Directory Information
--------

* [`training_wheels`](training_wheels)
    
    This is the main file of the __Training Wheels__ application. It is the most top-level [Python] script that creates and invokes all the other objects that allows the utility to run smoothly -- __this is the executable the user should run when they intend on using the program.__ It is to be excecuted by:

    ```
    ./training_wheels
    ```

* [`shell/`](shell/)
    
    This folder contains the "main loop" of the __Training Wheels__ tool and simulates the "shell," as is the point of the whole application. It handles the commands specific to the __Training Wheels__ shell and acts as the master object for all the code and objects given in the modules noted below.

* [`lessons/`](lessons/)
    
    This directory holds the backend [Python] source code to manage the "lessons" in the __Training Wheels__ shell, and contains the [`hjson`][hjson] and [JSON] files for the lessons themselves. It does act as a [Python] package and is necessary for __Training Wheels__ to run.

* [`save_engine/`](save_engine/)
    
    This folder contains the code to manage the saving and loading of the user's progress throughout their time with __Training Wheels__. It does act as a [Python] package and is necessary for __Training Wheels__ to run.

* [`colors/`](colors/)
    
    This folder acts as a [Python] package that offers the use of the [`colorama`][colorama] module with some convenient and easy-to-access shorthand functions. 

* [`_developer_`](_developer_)
    
    This directory holds code that is meant to be utilized by someone who plans on developing content for the __Training Wheels__ shell -- it includes some [`bash`][bash] scripts to install dependencies to build lesson files like [`nodejs`][nodejs], [`npm`][npm],  and [`hjson`][hjson]. 


[CTF]: https://ctftime.org/ctf-wtf/
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
[sqlite]: https://sqlite.org/
[sqlite3]: https://sqlite.org/
[HTTPS]: https://en.wikipedia.org/wiki/HTTPS