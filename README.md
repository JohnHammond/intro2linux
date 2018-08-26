Welcome to Linux!
========================

<p align="center">
  <img src="https://github.com/macee/linux_16/blob/master/pictures/tux.png?raw=true" alt="Tux, the Linux Mascot"/>
</p>

__[Linux]__ is a computer [operating system], much like [Microsoft Windows], which you are probably already used to working with. _But,_ it is designed for creative people who want to get work done -- engineers, mathematicians, scientists, developers, artists and more.

In this class, we'll be teaching you how to get started with the [Linux][Linux] [command-line], called [`bash`][bash]. You'll be exploring it all on the super-awesome-and-cheap microcomputer, the [Raspberry Pi].


<p align="center">
  <img src="https://github.com/macee/linux_16/blob/master/pictures/pi.jpg?raw=true" alt="The Raspberry Pi"/>
</p>


Please go ahead and explore. We'll be diving into more and more of these files as the weeks go on, but the point is to let you be inquisitive and creative -- so take a sneak peak, if you'd like. ;)

<p align="center">
  <img src="https://github.com/macee/linux_16/blob/master/pictures/raspberry.png?raw=true" alt="The Raspberry Pi Logo"/>
</p>

-----------------

Adding Material to github
------

To add files and material to [github], the commands follow the sequence of __add__, __commit__, and __push__.

Note that `git add .` will add the whole current directory. So if you are in the folder of your repo, it will collect all of the changes.

```
git add .
git commit
git push
```

---------------

Files & Directory Information
--------

[Linux] is all about "[open-source]", so we'll following the same mindset. Everything that was done in preparation for this class is available for you to see, if you are curious about it.

* [`setup/`](setup/)
    
    This folder holds all the files and code used to prepare for the "Intro to Linux" class. It goes over what was done to flash the [Raspbian] OS onto the [MicroSD] cards, and how we created all of the [github] repositories for each student.

* [`training_wheels/`](training_wheels/)
    
    In this directory is the source code and material for the "training wheels" [`bash`][bash] shell that was put together for this course, to create a more interactive learning experience. It was written in [Python] should continue to be maintained throughout the course.  

* [`scavenger_hunt/`](scavenger_hunt/)
    
    This directory holds all the source code for the "[Linux] Scavenger Hunt," which was an activity to practice working with files and folders and navigating through the [Linux] file system. It itself is a [Python] web application written with [Flask], using [JSON] to keep track of the challenges. 


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