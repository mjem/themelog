#!/usr/bin/env python

"""Log messages in different colours according to level.
Output can use 256 colours if the fabulous library is found.
"""

from __future__ import print_function

import os
import sys
import time
import logging
import logging.handlers
from datetime import datetime
from importlib import import_module

try:
	import fabulous
	# Why not try these for more terminal tricks.
	#  python -m fabulous.demo
	#  python -m fabulous.image <filename.png>
	#  python -m fabulous.text --skew=4 --shadow hello kitty

except ImportError:
	fabulous = None

# theme (module name from this directory) to use if not specified in init_log()
DEFAULT_THEME = os.environ.get('THEMELOG_THEME', 'base16')

# if THEMELOG_LIGHT is truthy we select a _light theme more suitable for terminals with
# light backgrounds
DEFAULT_LIGHT = False  # os.environ.get('THEMELOG_LIGHT', '').zfill(1)[0].lower() in ('t', '1')

# minimum log level to include
DEFAULT_LOG_LEVEL = 'DEBUG'

# date format
DEFAULT_DATEFMT = '%Y-%m-%d %H:%M:%S'

# message format used when a blank theme is selected or fabulous is not installed
# or stderr is being redirected
DEFAULT_MESSAGEFMT = '{r.asctime} {r.module} {r.levelname} {r.msg}'

# default number of days to hold logfiles for if rotating logfiles are configured
DEFAULT_ROTATING_COUNT = 90

# allow environment variable to switch on debug startup messages
DEFAULT_DEBUG_LOG = os.environ.get('THEMELOG_DEBUG', '').zfill(1)[0].lower() in ('t', '1')

# list available themes
SHOW_THEMES = os.environ.get('THEMELOG_SHOW_THEMES', '').zfill(1)[0].lower() in ('t', '1')


def get_messagefmt(theme, light=False, debug_log=False):
	"""Read messagefmt from modules in this directory.
	If `light` is true we look for a module named theme_light.py instead of theme.py.
	"""
	if fabulous is None or theme is None or not sys.stdout.isatty():
		# no terminal colours
		if debug_log:
			if fabulous is None:
				print('Disabling colour output because fabulous library not found')

			elif theme is None:
				print('Disabling colour output because chosen theme is null')

			else:
				print('Disabling colour output because stdout is not a terminal')

		return {None: DEFAULT_MESSAGEFMT}

	elif theme == '8bit' or os.environ.get('INSIDE_EMACS') is not None:
		if debug_log:
			if theme == '8bit':
				print('8-bit colour theme selected')

			else:
				print('8-bit colour theme forced as we are inside emacs ansi-term')

		# an 8-bit colour theme. Forced if we are running inside an emacs ansi-term shell.
		from themelog.themes import eightbit
		return eightbit.messagefmt

	else:
		if debug_log:
			print('Selected theme {t}'.format(t=theme))

		mod = None
		base = 'themelog.themes.{theme}'.format(theme=theme)
		if light:
			if debug_log:
				print('Seeking light theme')
			try:
				mod = import_module(base + '_light')

			except ImportError:
				pass

		if mod is None:
			try:
				mod = import_module(base)

			except ImportError:
				print('Cannot load module {base}'.format(base=base))
				show_available_themes()
				print('Disabling all color output')
				return {None: DEFAULT_MESSAGEFMT}

		return mod.messagefmt


class Formatter(object):
	"""Variation on logging.Formatter which uses different formats depending
	on the log level.
	"""
	def __init__(self, messagefmt, datefmt):
		self.messagefmt = messagefmt
		self.datefmt = datefmt

	def format(self, record):
		"""The following contents are available in the message:

			created 1374882991.29
			exc_info None
			exc_text None
			filename env.py
			funcName main
			levelname DEBUG
			levelno 10
			lineno 32
			module env
			msecs 291.249990463
			msg Hello I am debug message
			name root
			pathname /localhome/mje/Work/chart/chart/tools/env.py
			process 25037
			processName MainProcess
			relativeCreated 50.5659580231
			thread 139741536122624
			threadName MainThread

		Levels:
			debug
			info
			warning
			error
			critical

		"""
		# expand the message part if needed
		if '%s' in record.msg:
			record.msg = record.msg % record.args

		# look up the format string for this level
		messagefmt = self.messagefmt.get(record.levelname)
		if messagefmt is None:
			# use None if we have nothing configured for this level
			messagefmt = self.messagefmt[None]

		# format the message timestamp
		record.asctime = datetime.fromtimestamp(
			record.created).strftime(self.datefmt)

		# return the final assembled string
		return messagefmt.format(r=record)


def show_available_themes():
	"""Display list of available themes to console.
	Do not use logging here because the logging system will not be ready yet.
	"""
	print('Available themes:')
	for filename in os.listdir(os.path.join(os.path.dirname(__file__), 'themes')):
		if filename == '__init__.py':
			continue

		print('    {theme}'.format(theme=os.path.splitext(filename)[0]))


def init_log(theme=DEFAULT_THEME,
			 light=None,
			 level=DEFAULT_LOG_LEVEL,
			 logfile=None,
			 rotating_logfile=None,
			 rotating_logfile_count=DEFAULT_ROTATING_COUNT,
			 stdout=False,
			 tz=None,
			 datefmt=DEFAULT_DATEFMT,
			 debug_log=DEFAULT_DEBUG_LOG,
			 show_themes=SHOW_THEMES):
	"""Configure and initialise logging.

	Args:
		`theme` (str): Name of the theme (a module from this directory) to try to use.
		`light` (bool): Attempt to load a theme suitable for light coloured terminal backgrounds.
		`level` (str): Minimum message level.
		`logfile` (str): Write to single output log file instead of terminal.
		`rotating_logfile` (str): Write to daily rotating log files.
		`stdout` (bool): Write terminal log to stdout instead of stderr.
		`tz` (str or false): Set timezone for the process. If `tz` is False then use UTC.
		`datefmt` (str): Date format.
		`debug_log` (bool): Print trace messages showing how the logging is initialised.
		`show_themes` (bool): Print a list of available themes.
	"""

	if debug_log:
		print('Init of log')

	if show_themes:
		show_available_themes()

	# Set timezone
	if tz is not None:
		init_tz(tz)

	if light is None:
		light = DEFAULT_LIGHT

	# check for valid log level
	levels = ('DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL')
	if level not in levels:
		raise ValueError('level of {bad} not allowed, select from {good}'.format(
				bad=level, good=', '.join(levels)))

	# we configure the top level root logger
	logger = logging.getLogger()
	logger.setLevel(level)

	if logfile is not None:
		# single log file

		if debug_log:
			print('Writing log file to {path}'.format(path=logfile))

		filehandler = logging.FileHandler(logfile)
		filehandler.setFormatter(Formatter({None: DEFAULT_MESSAGEFMT},
										   datefmt))
		logger.addHandler(filehandler)

	elif rotating_logfile is not None:
		# rotating log file

		if debug_log:
			print('Writing rotating log file to {path}'.format(rotating_logfile))

		filehandler = logging.handlers.TimedRotatingFileHandler(
			filename=rotating_logfile,
			when='midnight',
			backupCount=rotating_logfile_count,
			utc=tz is False)
		filehandler.setFormatter(Formatter({None: DEFAULT_MESSAGEFMT},
										   datefmt))
		logger.addHandler(filehandler)

	else:
		# terminal

		if debug_log:
			print('Logging to terminal')

		if stdout:
			streamhandler = logging.StreamHandler(sys.stdout)

		else:
			streamhandler = logging.StreamHandler(sys.stderr)

		streamhandler.setFormatter(
			Formatter(get_messagefmt(theme, light, debug_log),
					  datefmt))
		logger.addHandler(streamhandler)

	# prevent doubling up of messages
	logger.propagate = False


def init_tz(tz):
	"""Use UTC time zone for logging.
	"""
	if tz is False:
		os.environ['TZ'] = 'UTC'  # required for scheduler and worker log timestamps

	else:
		os.environ['TZ'] = tz

	time.tzset()
