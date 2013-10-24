#!/usr/bin/env python

"""Write to daily rotating log files.
One message is written per minute so the rotation can be seen.
"""
import time
import logging
from themelog import init_log
logger = logging.getLogger()
init_log(rotating_logfile='test.log')
pause = 60
while True:
	logger.info('Sleeping for {pause} seconds'.format(pause=pause))
	time.sleep(pause)
