#!/usr/bin/env python

"""base16 colour theme requires 256-colour support.
"""

from fabulous import color as col

# Greyscale palette
# #000000
# #101010
# #202020
# #303030
# #404040
# #505050
# #606060
# #707070
# #808080
# #909090
# #a0a0a0
# #b0b0b0
# #c0c0c0
# #d0d0d0
# #e0e0e0
# #f0f0f0

# base16 palette
pal = {
	'base00': '#151515',
	'base01': '#202020',
	'base02': '#303030',
	'base03': '#505050',
	'base03.5': '#909090',
	'base04': '#b0b0b0',
	'base05': '#d0d0d0',
	'base06': '#e0e0e0',
	'base07': '#f5f5f5',
	'base08': '#ac4142',
	'base09': '#d28445',
	'base0A': '#f4bf75',
	'base0B': '#90a959',
	'base0C': '#75b5aa',
	'base0D': '#6a9fb5',
	'base0E': '#aa759f',
	'base0F': '#8f5536',
	}

messagefmt = {
	None: '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.fg256(pal['base03.5'], '{r.asctime}'),
		module=col.fg256(pal['base0D'], '{r.module}'),
		levelname=col.fg256(pal['base0C'], '{r.levelname}'),
		msg=col.fg256(pal['base0E'], '{r.msg}'),
		),
	'INFO': '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.fg256(pal['base03.5'], '{r.asctime}'),
		module=col.fg256(pal['base0D'], '{r.module}'),
		levelname=col.fg256(pal['base0B'], '{r.levelname}'),
		# levelname=col.fg256(pal['base06'], '{r.levelname}'),
		msg=col.fg256(pal['base0E'], '{r.msg}'),
		),
	'WARNING': '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.fg256(pal['base03.5'], '{r.asctime}'),
		module=col.fg256(pal['base0D'], '{r.module}'),
		levelname=col.fg256(pal['base0A'], '{r.levelname}'),
		msg=col.fg256(pal['base0E'], '{r.msg}'),
		),
	'ERROR': '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.fg256(pal['base03.5'], '{r.asctime}'),
		module=col.fg256(pal['base0D'], '{r.module}'),
		levelname=col.fg256(pal['base08'], '{r.levelname}'),
		msg=col.fg256(pal['base08'], '{r.msg}'),
		),
	'CRITICAL': '{asctime} {module} {levelname} {msg}'.format(
		asctime=col.fg256(pal['base03.5'], '{r.asctime}'),
		module=col.fg256(pal['base0D'], '{r.module}'),
		levelname=col.bold(col.fg256(pal['base08'], '{r.levelname}')),
		msg=col.bold(col.fg256(pal['base08'], '{r.msg}')),
		),
	}
