#!/usr/bin/env python

from distutils.core import setup

from themelog import __version__

setup(name='themelog',
	  version=__version__,
	  # py_modules=['themelog'],
	  description='256-colour log messages',
	  long_description=open('README.rst').read(),
	  author='Mike Elson',
	  author_email='mike.elson@gmail.com',
	  url='http://github.com/mjem/themelog',
	  packages=['themelog', 'themelog.themes'],
	  data_files=[('.', ['README.rst'])],
	  license='Apache-2',
	  requires=['fabulous'],
	  # install_requires=['fabulous'],
	  classifiers=[
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: Apache Software License',
		'Operating System :: POSIX :: Linux',
      ]
	  )
