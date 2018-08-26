The "Training Wheels" Shell
========================

<p align="center">
  <img src="https://github.com/macee/linux_16/blob/master/pictures/training_wheels.png?raw=true" alt="The bash shell"/>
</p>

To help you become a bit more acquainted with the [Linux][Linux] [command-line], the [`bash`][bash] shell, a _prototype_ idea is to let you interact with a "training wheels" shell, which tries to kind of hold your hand and guide you through running commands and learning different concepts in [Linux].

It is ___not___, by any means, a complete product or a one-size-fits-all utility. The hope is to see if this works well as a teaching tool -- if it fails and turns out to be a flop, we will move on from it or try a new tactic.

_But_, it is my hope, that this interactive tool will help ingrain commands and syntax into your head, and you will gain a better understanding of how things all fit together in the command-line. Please give feedback, comments, concerns and criticisms as they come to you.

__If this tool does turn out to be a success, I will add more content and "modules" to it as the weeks develop.__

---------------

Files & Directory Information
--------

* [`static/`](static/)
    
    This directory holds all of the static files used in the [Flask] web application, like the [CSS] stylesheet and [JavaScript] files. 


* [`templates/`](templates/)
    
    This folder contains all the [HTML] files used with [Flask]. They use the [Jinja2] template format, and all inherit from the `base_page.html` 

* [`lessons/`](lessons/)
    
    This directory holds the backend [Python] source code to manage the "lessons" in the __Training Wheels__ shell, and contains the [`hjson`][hjson] and [JSON] files for the lessons themselves. It does act as a [Python] package and is necessary for __Training Wheels__ to run.

* [`save_engine/`](save_engine/)
    
    This folder contains the code to manage the saving and loading of the user's progress throughout their time with __Training Wheels__. It does act as a [Python] package and is necessary for __Training Wheels__ to run.

* [`colors/`](colors/)
    
    This folder acts as a [Python] package that offers the use of the [`colorama`][colorama] module with some convenient and easy-to-access shorthand functions. 

* [`_developer_`](_developer_)
    
    This directory holds code that is meant to be utilized by someone who plans on developing content for the __Training Wheels__ shell -- it includes some [`bash`][bash] scripts to install dependencies to build lesson files like [`nodejs`][nodejs], [`npm`][npm],  and [`hjson`][hjson]. 



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
[colorama]: https://pypi.python.org/pypi/colorama
[nodejs]: https://nodejs.org/en/
[hjson]: https://hjson.org/
[npm]: https://www.npmjs.com/
[JSON]: http://www.json.org/
[CSS]: https://www.w3.org/Style/CSS/Overview.en.html
[JavaScript]: https://www.javascript.com/
[HTML]: https://en.wikipedia.org/wiki/HTML
[Jinja]: http://jinja.pocoo.org/