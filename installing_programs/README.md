Installing Programs
===========

> John Hammond | Monday, November 14th, 2016

---------------------------

Welcome back to __Intro to Linux__!

The goal for today is to get you familiar with the options that you have for _installing programs_  on a [Linux] computer. We're going to be running through a lot of cool stuff today, so please bear with me -- but hopefully it will be really insightful and you will understand everything along the way.

The Breakdown
--------------

So you have been using [Linux] on the [Raspberry Pi] all this time using the native and built-in programs and tools. That isn't so bad, because [Linux] already offers you all the awesome you need from the get-go (isn't your life complete with just [`bash`][bash] and [Python]?).... but _what if we want to install something new?_

To install something on a [Linux] computer, you basically have __two options__. [Linux] is very different than [Microsoft Windows] because you shouldn't really just go to a website to download and install something -- that's not safe. Who knows what people could put on the Internet? How can you trust what you are running on your computer, without knowing how it works and what is doing?

[Linux] solves this problem in two ways:

1. Installing software by compiling it from the raw and pure source code, so you can know and understand what the program is doing.
2. Only installing software from a trusted source specific for your distribution of [Linux]. This is called a __"[package repository]"__.

Since [Linux] is all about being [open-source], it makes for all of the software to be available in the form of just its source code.

Option 1: Source Code
===================

I want you to be able to understand this the way [Linux] wants you to understand everything. __From the bottom up.__

So; how can we get started learning how to _install a program_? 

Well, first... let's ___make our own program!___

Writing in C
------------

Most real and legitimate programs are written in a [programming language] like [C] or [C++]. The [Linux][Linux] [kernel], in fact, is written almost entirely in [C].

We've shown off [scripting languages] like [`bash`][bash] and [Python] in Intro to Linux, but we haven't touched compiled programs yet. Since we are learning how to _install programs_ now, there is no better time to look at how it is done for _our own_ programs!

Creating the Source Code
---------

In any directory of your choosing (maybe your [home directory] or the [temporary directory]), fire up a text editor to create a file with a `.c` extension. That's the file extension for [C] source code.

I'll use [`nano`][nano] for my text editor, as usual.

```
nano source_code.c
```

Now that we are in [`nano`][nano], we can start to write our `C` code. Many of you have this kind of syntax already, from when you used [C++] in ICP. Keep in mind that [C++] is just [C] with some more support for [object-oriented programming].

To be able to use some nice "in and out" functions that [C] offers for us, we will have to include that [standard library]. The "in and out" library for [C] is called [`<stdio.h>`][stdio.h]. You can include it with a special syntax called a [preprocessor directive], used with a notation starting with `#` and wrapping the library name in `<` and `>`.

``` c
#include <stdio.h>
```



We will need a `main` function for our program to execute. Since all programs have a [return code] within the [shell], the [return type] of the function should be `int`, for integer.

``` c
#include <stdio.h>

int main(){


}
```

The usual "Hello World!"
---------

We can have our program print to [standard output] with the [`puts`][puts] function. We'll just give it a string as an argument.

``` c
#include <stdio.h>

int main(){

    puts("Hi there!");

}
```

Well that is nice and all -- but it is pretty boring. Let's have [C] ask for our name. We will need to declare a variable, a character array with some bounded size (I'll use `20`, just arbitrarily...) that we can send the input to.

We can use the [`scanf`][scanf] to get user input, and we can specify that we want a string by using the special [format identifier] `%s`.

``` c
#include <stdio.h>

int main(){

    puts("Hi there!");
    puts( "What is your name?");

    char your_name[20];
    scanf( "%s", your_name );
    
    puts("Your name is...");
    puts( your_name );
    puts("... it is good to meet you!");
    
}
```

After you take the users name, you can print it out or do whatever you want with it. It's _your_ program!

Compiling your code
-------------

When you are done writing your code, you can break out of [`nano`][nano] with `Ctrl+X`.

At this point at the [command-line], you will want to __compile__ your program. This is unique to a _[programming language]_ ... you never _compile_ a [scripting language] like [Python] like this.

In [Linux], the most common [C] compiler is called [`gcc`][gcc], the ___[GNU] Compiler Collection___, with [GNU] being the backend project with [Linux]. It can _compile_ programs, much like the [Microsoft Visual Studio] that you are used to, except __it doesn't suck__ and it runs from the [command-line].

If you want, check out the [man page] for it!

```
man gcc
```

You should see it just takes the source code file as an argument. Here we go:

```
gcc source_code.c
```

If you don't have any typos or mistakes in your code, it should compile just fine. Take a look at your directory with [`ls`][ls].

You should see there is a new file, called [`a.out`][a.out]. It is already green, because it has been marked executable by default after compiling it. So you should be able to run it with the usual dot-slash syntax:

```
./a.out
```

Hopefully your program will run!

Now, you probably don't want your program's name to be [`a.out`][a.out]. If you want, you can remove the file with the usual

```
rm a.out
```

And when you compile your program, you can give another argument to [`gcc`][gcc] to specify the ___output file___. This will be the name of your program rather than the default [`a.out`][a.out]:

```
gcc source_code.c -o our_program
```

Then you should see it in the directory with [`ls`][ls], and should be able to run it 

```
./our_program
```

Automating the Compilation
=========================

___If___, you had a _much_ larger program that had lots of [dependencies] and other compilation flags and other management things for the development and creation for your software (i.e. if you were creating a legitimate program), you would typically take advantage of a [Linux] tool called [`make`][make].

[`make`][make] is what just about ___ALL___ legitimate and real software packages use to make the compilation and building of their software easy and simple. The idea is rather than just writing the crazy long 

```
gcc something.c dependency.c another_necessary_library.c -o something_else -O2 -Wall 
```

etcetera (and a bunch of other garbage) and when __not even knowing__ the source code files needed to compile someone elses program with, you could instead just run

```
make
```

and it would build all of the software for you!

This is done by creating specific ___rules___ and ___targets___ for the software, outlined in what is called a [`Makefile`][Makefile]. 

[`Makefile`][Makefile]s are put together with a-whole-nother language set and syntax -- but don't worry: it is easy. 

Creating a Makefile
---------

Let's start to build the [`Makefile`][Makefile] in [`nano`][nano]. 

```
nano Makefile
```

So the syntax for specifying a ___rule___ in a [`Makefile`][Makefile] starts with a __target__, or a file that you _want_ created. Since we are making a very simple program, all it is is just one executable binary... so we just have one __target__, and it should be what we want the name of the program to be.

Following the __target__ is a colon and a list of _dependencies_ that must exist and be used for the __target__ to be created. Again, since all we have is one source code file, we will just supply that.

```
our_program: source_code.c

```

This is the start of the ___rule___ for this __target__. To finish the ___rule___, we have to specify the [`bash`][bash] command that should be run in order to actually create or build the target. That is where our line from the [`gcc`][gcc] compiler comes in!

As good practice and to follow a common standard, it is typically a good idea to indent the command you use for the ___rule___. Make sure you do this with a `Tab` key, because the [`Makefile`][Makefile] uses that as a delimiter to detemrine the proper syntax. 

``` 
our_program: source_code.c
    gcc source_code.c -o our_program
```

At this point, you are practically done with the functionality you really need for the [`Makefile`][Makefile].

When you are ready, you can break out of [`nano`][nano] and the try and put together your program the _new_ way!

To verify things, you can remove the old program if you want and then run [`make`][make] to demonstrate the new automated compile.

```
make
```

It should display out the command that it is running, which in our case is the [`gcc`][gcc] command we put together. You should be able to [`ls`][ls] and see your program, and run it just like before!

```
./our_program
```

Adding a rule to "clean"
--------------

We can have our [`Makefile`][Makefile] be more flexible and do other things easily for us by adding more ___rules___. A very common ___rule___ to add is for a target `clean`, that will remove all of the binaries and perhaps any other dependencies that were built in the production of your project. 

In our case, because we have a very small program without any other dependencies, the only thing we could really "clean up" is the binary. So here is the syntax, back in our [`Makefile`][Makefile].

```
our_program: source_code.c
    gcc source_code.c -o our_program

clean: 
    rm our_program
```

See? The __target__ is `clean`, and there are no dependencies, and the command we want to run is the `rm` command like we have been using before.

Now, after you build and create your program with `make`, you can "clean up" at any point with `make clean`.

```
make
make clean
```

You just made a simple software package!
----------

Granted, our program is _incredibly_ small and serves no real purpose -- but we used it as a vessel to go through the process of using and understanding [`Makefile`][Makefile]s and some of the [C][C] [programming language].

Tarballs
=============

To make _one_ [compressed archive] with all of our source code and the `Makefile`, we can put together what is called a ___[tarball]___. 

A "[tarball]" is a [compressed archive] file, a lot like a [`.zip`][zip] file you have seen before. It is (arguably) the most common [compressed archive] filetype you will see on [Linux]. You can create and etxract [tarballs] with the [`tar`][tar] command.

You can check out the [man page] if you would like.

```
man tar
```

In all honesty, there is a running joke within the [Linux] community that no one really knows the proper [command-line] arguments to do things with [`tar`][tar]. There are so many options for parameters, people joke about just throwing letters together in the command and hoping it does what you want.

<p align="center">
  <img src="https://github.com/macee/linux_16/blob/master/pictures/tar.png?raw=true" alt="The Raspberry Pi"/>
</p>


Let's try and piece together what we need to be able to create our own [tarball], though.

Creating a tarball
-------

In our case, we want to _create_ a [compressed archive], so I'm sure you can see in the [man page] we need the `c` argument. 

We also want to specify the output file, or the name of the final [compressed archive][compressed archive] [tarball] that we want to create. Again, after checking the [man page], we can see we do this with the `f` argument.

Along with this, we want to be able to [`gzip`][gzip] compress our archive. This another common tactic with [Linux][Linux] [tarballs] and when you download source code packages to compile and install on your own. [gzip] is like the [GNU] version of the common [zip] archive. 

If you look in the [man page] you can see we need the `z` argument to be able to do this.

This means that after these arguments, we can specify the name of the new [compressed archive] file we want to create, and anything that follows will be added to the archive.

So in our case, to include the [`Makefile`][Makefile] and the source code:

```
tar cfz our_tarball.tar.gz  Makefile source_code.c
```

The common file extension usage for a [tarball] is a `.tar`, and when it is [gzip] compressed, the `.gz` extension tacked on at the end.

Now if you [`ls`][ls], you can see the `our_tarball.zip` file that has everything we need to build our program!

Extracting a tarball
----------------

So say you just received this [tarball], and you wanted to extract everything out of it. The [man page] says we do this with the `x` argument, and again using the `f` argument to specify the file name. 

```
tar xf our_tarball.tar.gz
```

That will extract out the [compressed archive]. If you want to be able to see what it is really doing or what files are being pulled out, you can also give it the `v` argument, for __verbose__.

```
tar xfv our_tarball.tar.gz
```

This will list out the files, and once you [`ls`][ls] you should be able to see them without a problem. Now you can [`make`][make] and run your program!

```
make
./our_program
```

Using a different archive & Makefile
================================

Now that you have created your very own "program," your own [`Makefile`][Makefile] and even the [tarball][tarball] [compressed archive] , I hope you understand those elements and how they make up a software package.

To go one step beyond, let's take a look at _someone elses's software_... a larger, legitimate program.

This is still a small program, it is just a [command-line] utility, but we can take a look at the source code and the [`Makefile`][Makefile] and everything.

Enter Figlet
-------

[`figlet`][figlet] is a [command-line] tool that will just take input text (passed as either an argument or entered as [standard input]) and blow it up into a larger, banner-style [ASCII] rendition of the text.

Right now, [`figlet`][figlet] shouldn't be installed. Go ahead and try to run [`figlet`][figlet] within the [command-line] and you ought to get an error:

```
figlet
```

```
figlet: command not found
```

So let's try and install it from source!

I have included the source code package in this repository (but you can just as easily [find it online on their website](ftp://ftp.figlet.org/pub/figlet/program/unix/figlet-2.2.5.tar.gz)), so if you haven't already, please pull all the changes for this repository and change directory into this folder.

```
cd linux_16
git pull
cd installing_programs
```

You should be able to [`ls`][ls] and you'll find the software package for [`figlet`][figlet], [`figlet-2.2.5.tar.gz`](figlet-2.2.5.tar.gz).

It's another [tar][tar] [compressed archive] with [gzip]! So, if you wanted to, you could extract it with 

```
tar xfv figlet-2.2.5.tar.gz
```

(Remember, using the `x` argument to eXtract and `f` to specify the File name. I use `v` to use Verbose mode and display all of the files being extracted.)

You can now change into the directory that it extracted out, `figlet-2.2.5`

```
cd figlet-2.2.5
```

Take a look around with [`ls`][ls].

```
CHANGES    crc.h        figlet.c   fonts      LICENSE      run-tests.sh    utf8.c
chkfont.6  FAQ          figlist    getopt.c   Makefile     showfigfonts    utf8.h
chkfont.c  figfont.txt  figlist.6  inflate.c  Makefile.tc  showfigfonts.6  zipio.c
crc.c      figlet.6     figmagic   inflate.h  README       tests           zipio.h
```

Hey, it's a whole software package, with legitmate software! It has lots of files and dependencies... a whole lot more than our "academic" testbed!

I recommend you explore for a bit. 

You should be able to see all the `.c` [C] source code files, and even the [`Makefile`][Makefile]. Go ahead and explore those things, to see someone elses code and what you can really do with these languages!

```
nano README
```

```
nano figlet.c
```

```
nano Makefile
```


If you take a look at the [`Makefile`][Makefile], you should see that the ___rules___ exist way down at the bottom of the file. At the top, there are a lot of comments and variables being set.

Make and Install
---------

When you are ready, go ahead and run

```
make
```

You should see your terminal slowly start to compile all the source code for the [`figlet`][figlet] program.

Once it is done (hopefully no errors), you can see new programs (the compiled `figlet` executable) in the local directory!

If you wanted to remove them you could run the usual `make clean`.

One of the most common __targets__ that is usually included in other software packages' [`Makefile`][Makefile] is `install`... `make install` will take the compiled program built after `make` and move it into your `PATH` variable, so you can easily run the program from the [command-line]. If you get an error like `Permission denied`, you should know you have to try and run it with `sudo`.

So here is the easy install and running...

```
make
sudo make install
figlet "Hello Linux!"
```

```
 _   _      _ _         _     _                  _ 
| | | | ___| | | ___   | |   (_)_ __  _   ___  _| |
| |_| |/ _ \ | |/ _ \  | |   | | '_ \| | | \ \/ / |
|  _  |  __/ | | (_) | | |___| | | | | |_| |>  <|_|
|_| |_|\___|_|_|\___/  |_____|_|_| |_|\__,_/_/\_(_)
                                                   
```

Option 2: Package Repositories
============

The _other_ option for installing software in [Linux].... which is admittedly more user-friendly and done more often... is using a package repository to download, install, and configure your programs and even handle and keep track of dependencies.

The interesting thing is, that with each [Linux distribution] there is typically a different ___[package manager]___, which is the tool that lets you interact with these package repositories (or "repos" for short).

In [Debian] based systems, like [Ubuntu] and even [Raspbian], the [distribution] used on the [Raspberry Pi], the __[package manager]__ is called [`apt`][apt], or the Advanced Packaging Tool. 

The __[package manager]__ keeps track of all of the different repos that the [distribution] trusts... and of course, you as the user can customize it and an add and remove repos as you please, to have access to other software packages if you need to.

Occasionally the __[package manager]__ has to be updated, so it has the most recent software. For [Raspbian], the command is `apt update`.

__Note that because the [package manager] is installing things and making changes to the computer and the file system, it must always be run as `root` or with `sudo`__.

```
sudo apt update
```

___Updating and installing software on a [Raspberry Pi] through [`apt`][apt] is pretty slow. Don't be worried if it takes a while.___

Now, when you want to actually install a program or some new software, you must know the _exact name_ of the package you want to install.

To try and find the software you are looking for, you can search the repositories, with a variation of the [`apt`][apt] command: `apt-cache search`. You can offer a search term for it to look for and the __package manager__ will try and find software packages with info concerning it.

So, let's say I wanted to some software that has to do with ___cows___, I could run:

```
sudo apt-cache search cow
```

And I could peruse and look through some small descriptions as to what the returned packages are and contain.

Say I found what I was looking for, and I wanted to install the [`cowsay`][cowsay] package.

```
sudo apt install cowsay
```

___Updating and installing software on a [Raspberry Pi] through [`apt`][apt] is pretty slow. Don't be worried if it takes a while.___

You can just run the [`apt`][apt] command with an `install` argument, and the name of the package. In this case, it is just the name of the software: [`cowsay`][cowsay].

The __[package manager]__  should update your `PATH` variable so you can use any installed software right away.

```
cowsay "Hello Linux!"
```

```
 ______________
< Hello Linux! >
 --------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

You have now installed a program! 

Aftermath
=============

You've now done this two ways: from "scratch," handling a software package and code and a program all on your own... and using a [package manager] to handle everything for you in just one easy command.

In reality, you will likely find yourself installing things and working with software through the repositories and the [package manager] like [`apt`][apt], but understanding how to [`make`][make] and configure a package of source code from a [tarball] is an incredible [Linux] skill that will come in handy if ( er, _when_ ) the repositories fail you.



[github]: http://github.com
[MicroSD]: https://en.wikipedia.org/wiki/MicroSD
[Raspbian]: https://www.raspberrypi.org/downloads/raspbian/
[operating system]: https://en.wikipedia.org/wiki/Operating_system
[operating systems]: https://en.wikipedia.org/wiki/Operating_system
[github]: https://github.com/
[bash]: https://en.wikipedia.org/wiki/Bash_(Unix_shell)
[IMG]: https://en.wikipedia.org/wiki/IMG_(file_format)
[Linux]: https://en.wikipedia.org/wiki/Linux
[Microsoft Windows]: https://en.wikipedia.org/wiki/Microsoft_Windows
[Windows]: https://en.wikipedia.org/wiki/Microsoft_Windows
[command-line]: https://en.wikipedia.org/wiki/Command-line_interface
[shell]: https://en.wikipedia.org/wiki/Command-line_interface
[command line]: https://en.wikipedia.org/wiki/Command-line_interface
[Raspberry Pi]: https://www.raspberrypi.org/
[open-source]: https://en.wikipedia.org/wiki/Open-source_software
[Python]: https://www.python.org/
[github]: https://github.com
[JSON]: http://www.json.org/
[Flask]: http://flask.pocoo.org/
[SHA1]: https://en.wikipedia.org/wiki/SHA-1
[nano]: https://en.wikipedia.org/wiki/GNU_nano
[shabang]: https://en.wikipedia.org/wiki/Shebang_(Unix)
[shebang]: https://en.wikipedia.org/wiki/Shebang_(Unix)
[she-bang]: https://en.wikipedia.org/wiki/Shebang_(Unix)
[sha-bang]: https://en.wikipedia.org/wiki/Shebang_(Unix)
[sha-bang line]: https://en.wikipedia.org/wiki/Shebang_(Unix)
[she-bang line]: https://en.wikipedia.org/wiki/Shebang_(Unix)
[chmod]: https://en.wikipedia.org/wiki/Chmod
[scripting language]: https://en.wikipedia.org/wiki/Scripting_language
[scripting languages]: https://en.wikipedia.org/wiki/Scripting_language
[programming language]: https://en.wikipedia.org/wiki/Programming_language
[command substitution]: http://mywiki.wooledge.org/CommandSubstitution
[standard output]: https://en.wikipedia.org/wiki/Standard_streams#Standard_output_.28stdout.29
[standard input]: https://en.wikipedia.org/wiki/Standard_streams
[standard error]: https://en.wikipedia.org/wiki/Standard_streams#Standard_error_.28stderr.29
[file descriptor]: https://en.wikipedia.org/wiki/File_descriptor
[package repository]: https://en.wikipedia.org/wiki/Software_repository
[software repository]: https://en.wikipedia.org/wiki/Software_repository
[C]: https://en.wikipedia.org/wiki/C_(programming_language)
[C++]: https://en.wikipedia.org/wiki/C%2B%2B
[kernel]: https://en.wikipedia.org/wiki/Linux_kernel
[object-oriented programming]: https://en.wikipesdia.org/wiki/Object-oriented_programming
[OOP]: https://en.wikipedia.org/wiki/Object-oriented_programming
[return code]: https://en.wikipedia.org/wiki/Exit_status
[exit status]: https://en.wikipedia.org/wiki/Exit_status
[return type]: https://en.wikipedia.org/wiki/Return_type
[puts]: https://www.tutorialspoint.com/c_standard_library/c_function_puts.htm
[scanf]: https://www.tutorialspoint.com/c_standard_library/c_function_scanf.htm
[format specifiers]: http://www.codeforwin.in/2015/05/
[format identifier]: http://www.codeforwin.in/2015/05/
[format identifiers]: http://www.codeforwin.in/2015/05/list-of-all-format-specifiers-in-c.html
[format specifier]: http://www.codeforwin.in/2015/05/list-of-all-format-specifiers-in-c.html
[standard library]: https://en.wikipedia.org/wiki/Standard_library
[stdio.h]: https://www.tutorialspoint.com/c_standard_library/stdio_h.htm
[preprocessor directive]: http://www.cprogramming.com/reference/preprocessor/
[preprocessor]: https://en.wikipedia.org/wiki/Preprocessor
[gcc]: https://gcc.gnu.org/
[GNU]: https://www.gnu.org/home.en.html
[man page]: https://en.wikipedia.org/wiki/Man_page
[ls]:http://linuxcommand.org/man_pages/ls1.html
[a.out]: https://en.wikipedia.org/wiki/A.out
[dependencies]: http://askubuntu.com/questions/361741/what-are-dependencies
[dependency]: http://askubuntu.com/questions/361741/what-are-dependencies
[make]: https://www.gnu.org/software/make/
[Makefile]: https://en.wikipedia.org/wiki/Makefile
[zip]: https://en.wikipedia.org/wiki/Zip_(file_format)
[archive file]: https://en.wikipedia.org/wiki/Archive_file
[compressed archive]: https://en.wikipedia.org/wiki/Archive_file
[tar]: https://en.wikipedia.org/wiki/Tar_(computing)
[tarball]: https://en.wikipedia.org/wiki/Tar_(computing)
[tarballs]: https://en.wikipedia.org/wiki/Tar_(computing)
[gzip]: https://en.wikipedia.org/wiki/Gzip
[figlet]: http://www.figlet.org/
[ASCII]: https://en.wikipedia.org/wiki/ASCII
[Linux distribution]: https://en.wikipedia.org/wiki/Linux_distribution
[distribution]: https://en.wikipedia.org/wiki/Linux_distribution
[package manager]: https://en.wikipedia.org/wiki/Package_manager
[Ubuntu]: https://www.ubuntu.com/
[Debian]: https://www.debian.org/
[apt]: https://en.wikipedia.org/wiki/Advanced_Packaging_Tool
[apt-get]: https://en.wikipedia.org/wiki/Advanced_Packaging_Tool
[cowsay]: https://en.wikipedia.org/wiki/Cowsay
[home directory]: https://en.wikipedia.org/wiki/Home_directory
[temporary folder]: https://en.wikipedia.org/wiki/Temporary_folder
[temporary directory]: https://en.wikipedia.org/wiki/Temporary_folder
[Microsoft Visual Studio]: https://en.wikipedia.org/wiki/Microsoft_Visual_Studio