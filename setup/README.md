Setting up for "Intro to Linux"
========================

> John Hammond | Friday, August 18th 2016
 
---------------------------------------------------------

This directory is to house and document all the files made and processes to prepare for and set up the 2016 "Intro to Linux" course. This pretty much consists of ...

* Flashing the [MicroSD] cards with the [Raspbian][Raspbian] [operating system].
* Creating a [github] repository for each individual student.



Files & Directory Information
--------------

* [`build_raspbian.sh`](build_raspbian.sh)
    
    This is a simple [`bash`][bash] script that bundles the instructions given to [flash Raspbian on a MicroSD from Linux](https://www.raspberrypi.org/documentation/installation/installing-images/linux.md). It checks to see if there is the [`.img`][IMG] file in the current directory (__`2016-05-27-raspbian-jessie.img`__ at the time of writing, the most recent version) -- if it does not see it, it will download it and continue.


[MicroSD]: https://en.wikipedia.org/wiki/MicroSD
[Raspbian]: https://www.raspberrypi.org/downloads/raspbian/
[operating system]: https://en.wikipedia.org/wiki/Operating_system
[operating systems]: https://en.wikipedia.org/wiki/Operating_system
[github]: https://github.com/
[bash]: https://en.wikipedia.org/wiki/Bash_(Unix_shell)
[IMG]: https://en.wikipedia.org/wiki/IMG_(file_format)