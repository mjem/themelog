#!/usr/bin/env python

"""base16 colour theme requires 256-colour support.
"""

from fabulous import color as col

from themelog.themes.base16 import pal

messagefmt = {
	None: '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.fg256(pal['base03'], '{r.asctime}'),
		module=col.fg256(pal['base03.5'], '{r.module}'),
		levelname=col.fg256(pal['base0C'], '{r.levelname}'),
		msg=col.fg256(pal['base02'], '{r.msg}'),
		),
	'INFO': '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.fg256(pal['base03'], '{r.asctime}'),
		module=col.fg256(pal['base03.5'], '{r.module}'),
		levelname=col.fg256(pal['base0B'], '{r.levelname}'),
		# levelname=col.fg256(pal['base06'], '{r.levelname}'),
		msg=col.fg256(pal['base02'], '{r.msg}'),
		),
	'WARNING': '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.fg256(pal['base03'], '{r.asctime}'),
		module=col.fg256(pal['base03.5'], '{r.module}'),
		levelname=col.fg256(pal['base0A'], '{r.levelname}'),
		msg=col.fg256(pal['base02'], '{r.msg}'),
		),
	'ERROR': '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.fg256(pal['base03'], '{r.asctime}'),
		module=col.fg256(pal['base03.5'], '{r.module}'),
		levelname=col.fg256(pal['base08'], '{r.levelname}'),
		msg=col.fg256(pal['base08'], '{r.msg}'),
		),
	'CRITICAL': '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.fg256(pal['base03'], '{r.asctime}'),
		module=col.fg256(pal['base03.5'], '{r.module}'),
		levelname=col.bold(col.fg256(pal['base08'], '{r.levelname}')),
		msg=col.bold(col.fg256(pal['base08'], '{r.msg}')),
		),
	}
