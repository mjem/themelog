#!/usr/bin/env python

"""Colour theme for terminals which support only 8-bit colors.
"""

from fabulous import color as col

messagefmt = {
	None: '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.highlight_blue('{r.asctime}'),
		module=col.cyan(('{r.module}')),
		levelname=col.cyan('{r.levelname}'),
		msg=col.bold(col.yellow('{r.msg}')),
		),

	'INFO': '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.highlight_blue('{r.asctime}'),
		module=col.cyan(('{r.module}')),
		levelname=col.green('{r.levelname}'),
		msg=col.bold(col.yellow('{r.msg}')),
		),

	'WARNING': '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.highlight_blue('{r.asctime}'),
		module=col.cyan(('{r.module}')),
		levelname=col.bold(col.magenta('{r.levelname}')),
		msg=col.bold(col.yellow('{r.msg}')),
		),

	'ERROR': '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.highlight_blue('{r.asctime}'),
		module=col.cyan(('{r.module}')),
		levelname=col.red('{r.levelname}'),
		msg=col.red('{r.msg}'),
		),

	'CRITICAL': '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.highlight_blue('{r.asctime}'),
		module=col.cyan(('{r.module}')),
		levelname=col.bold(col.red('{r.levelname}')),
		msg=col.red('{r.msg}'),
		),
	}
