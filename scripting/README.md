Bash Scripting
===========

> John Hammond | Thursday, October 20th, 2016

---------------------------

Welcome back to __Intro to Linux__!

Today we hope to get our hands dirty with [`bash`][bash] shell scripting. This document should hopefully act as a "Getting Started" guide or at least a reference.

Let's get started!
==============

All [`bash`][bash] scripts are plain text files. They are multiple [`bash`][bash] [Linux] commands grouped and put in sequence, much a like "script" for an interpreter to read. 

Typically [`bash`][bash] scripts are files that end in a `.sh` extension. Since in [Linux], file types are not determined by simply an extension, so the `.sh` is really optional -- but it is a good idea to include it regardless.

```
nano my_script.sh
```

You should be thrown into [`nano`][nano], the [command-line] text editor with a new file open.

The Sha-Bang Line
-----------

All scripts in [Linux] start with a very special line that tell [Linux] what program or binary to associate this file with. It tells [Linux] what "interpreter" should be the one to read the script, so in our case, we want [`bash`][bash]! This special line is called the [sha-bang line].

The syntax for the [sha-bang line] is a special notation with `#!` followed by the path of the program you want to execute the script. So, if we want [`bash`][bash] to run it, where does [`bash`][bash] live in our file system?

```
$ which bash
/bin/bash
```

Right, the path is `/bin/bash`. So, the first line of our script should look like this with the [sha-bang line]:

``` 
#!/bin/bash
```

Now [Linux] should know to give the script to [`bash`][bash] once we execute the it.

Saying "Hello, World"
---------------

It's a rite of passage for a programmer to write his or her first "Hello World" program. Since working with standard output is insanely easy in [`bash`][bash], we will just add that one line. Our script should now look like:

``` bash
#!/bin/bash 

echo "Hello, World"
```

And that's all we need for now!

Running a Script
-------

When you are all done editing your script, you can use `Ctrl`+`X` to exit [`nano`][nano]. Now at your prompt, you can run your script by using that `./` syntax like usual. Remember that means that _in this current directory_, I want to run _this file/program_.

```
$ ./my_script.sh
bash: ./my_script.sh: Permission denied
```

Woah woah woah, ___permission denied??!!___ What the heck, right? ___We___ own the file, it is ours, we should be able to do anything we want with it, right?

Check out the `ls -l` output again to look at the file permissions.

```
$ ls -l
-rw-rw-r--  1 john john    33 Oct 20 17:05 my_script.sh
```

... Do you see what is missing?

We have _read_ and _write_ permission bits set, but we don't have _execute_. By default, we can't execute our script! 

The way we can make it executable in [Linux] is with the [`chmod`][chmod] command. We can use it modify the file permission bits on some files; we can add or remove `r`, or `w`, or `x`, just like you've seen with `ls -l`.

So the syntax in this case is:

```
$ chmod +x my_script.sh
```

Now you should be able to _execute_ your script just fine!

```
$ ./my_script.sh 
Hello, World
```

Sweet! That's the absolute basics of getting a script running. Now you'll want to do interesting things, one after another, to automate tasks very quickly.

Other Logic
==========

Since [`bash`][bash] is a [scripting language], it has other functionality to do things and branch out logic flow like any regular [programming language].

Comments
------------

The syntax for a comment in [`bash`][bash] is a simple pound symbol.

``` bash
#!/bin/bash

# comment/note to self: actually add code that will do valuable things
echo "This is code does nothing interesting."
```

Variables
-------------

Variables can be set like a normal expression in mathematics, and their value can be accessed by prefxing their name with a dollar sign `$`. Since [`bash`][bash] tokenizes commands and arguments by spaces, ___avoid placing spaces between your variable name, the equals sign, and the variable value___.

``` bash
#!/bin/bash

my_name="John Hammond"

echo "Hello, my name is $my_name".
```

Command Substitution
-----------

In [`bash`][bash], there is a handy thing called [_command substitution_][command substitution], which inserts the [standard output] of a certain  command wherever you used the substitution.

The syntax for it is wrapping the command in backticks, like ``ls`` or with a dollar sign `$` and parentheses: `$(ls)`

This is handy for storing the output of a command in a variable or to process later.

``` bash
#!/bin/bash

contents_of_directory=`ls`

echo "The contents of this directory are:"
echo $contents_of_directory
```

Catching User Input
-----------

Typically in a program you do want to prompt for user input, and store what they entered into a variable, so you can work with it later on throughout the program.

You can accomplish this in [`bash`][bash] with the `read` command, and by passing it an argument for the name of the variable you want to store the result in.

``` bash
#!/bin/bash

echo "What is your name?"

read your_name

echo "Hello $your_name, it is good to meet you."
```

Hiding Command Output
--------------------

Sometimes, for your automation and your scripting, you want to throw away your command output. Sometimes you may have tools that spew things out on the [standard output] or the [standard error] stream and you want to hide it, so your own script output is much cleaner.

You can do this with redirection (remember the `>` symbol) and by taking advantage of a special "device" on your [Linux] computer: `/dev/null`. Try and think of this special path as like a black hole; a digital trash can; anything that goes into it, is gone.

In [`bash`][bash], you can redirect [standard output] of a command like this:

``` bash
ls > /dev/null
```

The [standard output] stream has the [file descriptor] of number `1`. [Standard error] has the number `2`, so if we wanted to get rid of [standard error], we would specify:

```
ls 2> /dev/null
```

In this case, ___MAKE SURE___ there is no space between the number `2` and the  `>` redirection symbol. This is so the shell does not tokenize the entry and interpret the number `2` as a separate command.

But what if we wanted to get rid of ___BOTH___ [standard output] AND [standard error]? Well, you can redirect the output of one stream to go to the same location as the other stream by denoting it with a `&` symbol. Here is how the syntax looks:

```
ls > /dev/null 2>&1
```

Again, ___do not___ have any spaces between the characters `2>&1`. This helps [Linux] identify that you are really trying to redirect [standard error] to [standard output].

``` bash
#!/bin/bash

echo "This command, 'ls', will display output!"
ls

echo "This command, 'ls > /dev/null 2>&1', will NEVER display any output!"
ls > /dev/null 2>&1
```

Functions
----------

Functions in [`bash`][bash] are declared with the simple keyword: `function`

``` bash
#!/bin/bash

function say_hello(){
	echo "Hello everybody."
}

say_hello
```

They are called like a command, without explicity putting parentheses or any special formatting -- just the name of the function.


To work with arguments, you can access their variables in the body of the function by specifying a variable based off a number.
The first argument will be `$1`, the second will be `$2`, and so on.

``` bash
#!/bin/bash

function say_hello_to_someone(){
	echo "Hello $1."
}


say_hello_to_someone "LT Wyman"
```


The If Statement
--------

Here's the syntax for a typical `if` statement in [`bash`][bash]. 

``` bash
if [ CONDITION ]
then
    # EXECUTE YOUR
    # CODE STATEMENTS
    # HERE IN THIS BLOCK
fi
```


For [`bash`][bash], there are special notations that must be used inside of your condition. __For a more definitive example of how to work with the `if` statement in [`bash`][bash], please check out this link: [`http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_01.html`](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_01.html)__

The For Loop
-------

The `for` loop in [`bash`][bash] can also take on many syntax styles.

For counting...

``` bash
#!/bin/bash

for i in {1..10}
do
    # print the numbers 1 through 10
    echo $i
done
```

And for iterating over values in a list...

``` bash
#!/bin/bash

for line in `ls`
do
    # print each line of the standard output that the ls command produces
    echo $line
done
```

The While Loop
------

The `while` loop in [`bash`][bash] has the same structure as the `if` statement:

``` bash
while [ CONDITION ]
do
    # EXECUTE YOUR
    # COMMANDS HERE
    # IN THIS BLOCK
done
```

For more definitive uses and examples, [try doing some research of your own](https://linux.die.net/Bash-Beginners-Guide/sect_09_02.html).

The `while` loop does have a very special use case, when you want to on-the-fly loop through the output of a command. __This is a powerful technique__. You can do this by combining the `while` loop and the `read` command, even piping into `while` loop syntax. Check it out:

``` bash
#!/bin/bash

ls | while read line
do
    # This will run the `file` command on every single item in the directory
    file $line
done
```


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
[command-line]: https://en.wikipedia.org/wiki/Command-line_interface
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
[programming language]: https://en.wikipedia.org/wiki/Programming_language
[command substitution]: http://mywiki.wooledge.org/CommandSubstitution
[standard output]: https://en.wikipedia.org/wiki/Standard_streams#Standard_output_.28stdout.29
[standard error]: https://en.wikipedia.org/wiki/Standard_streams#Standard_error_.28stderr.29
[file descriptor]: https://en.wikipedia.org/wiki/File_descriptor
