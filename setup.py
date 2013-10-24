#!/usr/bin/env python

from distutils.core import setup

from themelog import __version__

setup(name='themelog',
	  version=__version__,
	  description='256-colour log messages',
	  author='Mike Elson',
	  author_email='mike.elson@gmail.com',
	  url='github.com/mjem/themelog',
	  packages=['themelog'],
	  classifiers=[
		'Development Status :: 4 - Beta',
		'Environment :: X11 Applications :: GTK',
		'Intended Audience :: End Users/Desktop',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: GNU General Public License (GPL)',
		'Operating System :: POSIX :: Linux',
		'Programming Language :: Python',
		'Topic :: Desktop Environment',
		'Topic :: Text Processing :: Fonts'
      ]
	  )
