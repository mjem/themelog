themelog
========

Intro
-----

themelog is a module which sets the colour of Python terminal logging messages according to severity, using a choice of 8- and 256-colour themes. By default a colour set using 256-colour codes is used based on the base16 theme.

Example
-------

A piece of code using the library:

  .. code:: python

	import logging
	from themelog import init_log
	logger = logging.getLogger()
	init_log()
	logger.info('Imported themelog library')
	logger.info('Created logger')
	logger.info('Initialised logging system')
	logger.debug('This is a debug message')
	logger.info('This is a info message')
	logger.warning('This is a warning message')
	logger.error('This is a error message')
	logger.critical('This is a critical message')


And the resulting output:

  .. image:: img/screenshot.png
    :width: 400px
    :target: img/screenshot.png

Usage
-----

Call ``init_log()`` function to enable themelog with the following optional parameters:

theme
  (*str*) Name of the theme to load.

light
  (*bool*) Attempt to load a version of the theme suitable for terminals with a light background colour.

level
  (*str*) Set to 'DEBUG', 'INFO', 'WARN', 'ERROR' or 'CRITICAL' to specify minumim message level that will be logged.

logfile
  (*str*) Write output to a single log file instead of console.

rotating_logfile
  (*str*) Write output to daily rotating log files.

rotating_logfile_count
  (*int*) Specify number of days to retain daily log files (default: 90).

stdout
  (*bool*) Write terminal log to stdout instead of stderr.

tz
  (*str*) Force the timezone to use for messages. Set to False for UTC.

datefmt
  (*str*) Date format.

debug_log
  (*bool*) Print trace messages showing how the logging is initialised.

show_themes
  (*bool*) Print a list of available themes.

Themes
------

Themes can be selected either via a parameter to the ``init_log`` call or by setting the environment variable THEMELOG_THEME.

To see a list of available themes either look in the ``themes`` directory, or set "list_themes" to True when calling ``init_log()``, or set the environment variable THEMELOG_THEMES before running the application.

Piped output
------------

Colours are disabled if standard output is not a terminal.

Environment variables
---------------------

You can set the following environment variables before startup to configure the process:

**THEMELOG_THEME**
  Select the name of the theme to use.

**THEMELOG_DEBUG**
  Show additional debug messages on startup. Debug messages are written to standard output using normal print statements because they are generated before the logging system is initialised.

**THEMELOG_SHOW_THEMES**
  List all available themes.

Requirements
------------

themelog uses the `fabulous <http://lobstertech.com/fabulous.html>`_ library to generate escape codes.

Compatibility
-------------

This code has been tested under Linux and using Python 2.7 only.

Thanks
------

The base16 theme was designed by Chris Kempson https://github.com/chriskempson/base16.

Legal
-----

themelog is copyright 2013 Mike Elson

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this software except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

..
    Local Variables:
    mode: rst
    coding: utf-8
    indent-tabs-mode: t
    tab-width: 4
    sentence-end-double-space: nil
    fill-column: 80
    End:
