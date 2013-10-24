#!/usr/bin/env python

"""Write to single logfile.
"""
import logging
from themelog import init_log
logger = logging.getLogger()
init_log(logfile='test.log')
logger.debug('This is a debug message')
logger.info('This is a info message')
logger.warning('This is a warning message')
logger.error('This is a error message')
logger.critical('This is a critical message')
