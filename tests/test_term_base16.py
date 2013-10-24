#!/usr/bin/env python

"""Log to terminal using default base16 theme.
"""

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
