#!/usr/bin/env python

"""Messages are written to stdout instead of the normal stderr.
"""
import logging
from themelog import init_log
logger = logging.getLogger()
init_log(stdout=True)
logger.debug('This is a debug message')
logger.info('This is a info message')
logger.warning('This is a warning message')
logger.error('This is a error message')
logger.critical('This is a critical message')
