#!/usr/bin/env python

"""The very special "rubble" theme.
"""

from fabulous import color as col

pal = {
	'39m': '#0d1926',
	'40m': '#161616',
	'41m': '#a45f1a',
	'42m': '#1aa45f',
	'43m': '#5fa41a',
	'44m': '#5f1aa4',
	'45m': '#a41a5f',
	'46m': '#1a5fa4',
	'47m': '#dfdfdf',
	}

messagefmt = {
	None: '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.fg256(pal['44m'], '{r.asctime}'),
		module=col.fg256(pal['44m'], '{r.module}'),
		levelname=col.fg256(pal['44m'], '{r.levelname}'),
		msg=col.fg256(pal['44m'], '{r.msg}'),
		),
	'INFO': '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.fg256(pal['43m'], '{r.asctime}'),
		module=col.fg256(pal['43m'], '{r.module}'),
		levelname=col.fg256(pal['43m'], '{r.levelname}'),
		msg=col.fg256(pal['43m'], '{r.msg}'),
		),
	'WARNING': '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.fg256(pal['41m'], '{r.asctime}'),
		module=col.fg256(pal['41m'], '{r.module}'),
		levelname=col.fg256(pal['41m'], '{r.levelname}'),
		msg=col.fg256(pal['41m'], '{r.msg}'),
		),
	'ERROR': '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.fg256(pal['45m'], '{r.asctime}'),
		module=col.fg256(pal['45m'], '{r.module}'),
		levelname=col.fg256(pal['45m'], '{r.levelname}'),
		msg=col.fg256(pal['45m'], '{r.msg}'),
		),
	'CRITICAL': '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.fg256(pal['45m'], '{r.asctime}'),
		module=col.fg256(pal['45m'], '{r.module}'),
		levelname=col.bold(col.fg256(pal['45m'], '{r.levelname}')),
		msg=col.bold(col.fg256(pal['45m'], '{r.msg}')),
		),
	}
