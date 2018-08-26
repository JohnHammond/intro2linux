Scripting Playground
============

> John Hammond | Thursday, October 20th, 2016

---------------------------------

Background
-----

This [github] repository aims to house all the "flag programs" used in an exercise for the "Intro to Linux" class.

The idea is to use [`git`][github] as a vessel to teach [`bash`][bash] scripting. In some commits, there is an executable file, that once run, will yield a flag based off of the current time. The goal is to write a script that will run through each commit, run each program, and submit each flag -- each minute.

This could be done by hand of course, but it would be tedious and not very fruitful in regard to the game. So, the more you can script, the more you win! :D

Viewing Commits
------

Once you have cloned a repository ( with `git clone`, remember? ) you can view all of the commits by another command:

```
git log
```

This should show you all of the commits and the commit messages by a unique identifier that [`git`][github] uses, a simple [SHA1] hash.

You can zoom in one specific commit with a command like 

```
git show [SHA1_HASH]
```

and by passing in the [SHA1] hash (like `d8328bf9bc010d9e2c48ae4bdd296d465686f3df` as an example) as the last argument.

Typically you can take advantage this to view some of the plaintext files that have been modified throughout the lifetime of a [github] repo. Since we want to be looking at the files and running the programs, we won't need this for "the game". 

--------------

Switching to a different commit
-------

For the purposes of "the game," you will want to go back in time and _revisit_ all the old commits, to find the flag programs. You can do this with the syntax:

```
git checkout [SHA1_HASH]
```

Now the repository that you see may change, because you switched back to that "version" of the repository (or the state of the repository at the time of that commit).

If you run `git log` now, though, you will __not__ be able to see the commits that happened _after_ the current commit you are on! Since you are only looking at a "log" of things that happened in the past, and you have _already moved to some point in the past_, you can't see the stuff inbetween then and now.

So, we need a different command.

```
git rev-list --remotes
```

[`git rev-list --remotes`](https://git-scm.com/docs/git-rev-list) will work similar to `git log`, but this will instead show _all_ commits with only the identifying [SHA1] hash.

That should give you enough to start to poke at the old commits. 

But to get rolling with the scripting... __can you think of a recipe to loop through all of the commit [SHA1] hashes and _check out_ each one? How can you run the program from there?__

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
[zombie link]: iusethistorapidlydevelopnewcommits:__