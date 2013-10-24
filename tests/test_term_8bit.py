#!/usr/bin/env python

"""Log to terminal using 8-bit theme.
"""

import logging
from themelog import init_log
logger = logging.getLogger()
init_log('8bit')
logger.debug('This is a debug message')
logger.info('This is a info message')
logger.warning('This is a warning message')
logger.error('This is a error message')
logger.critical('This is a critical message')
