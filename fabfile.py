#!/usr/bin/env python

from fabric.api import local
from fabric.api import lcd

def sdist():
	"""Make a source distribution."""
	local('python setup.py sdist')

# def archive():
	# """Make a tarball of the mercurial source repository."""
	# local('tar cf themelog.hg.tar.bz2 .hg')

def archive():
	"""Make a tarball of the mercurial source repository."""
	local('tar cf themelog.git.tar.bz2 .git')

# def dist():
	# """Make a tarball of the tracked files."""
	# local('hg archive themelog.tar.bz2')

def dist():
	"""Make a tarball of the tracked files."""
	local('git archive themelog.tar.bz2')

def pylint():
	"""Run pylint over all files."""
	local('pylint fabfile.py themelog test')

def pep8():
	"""Run pep8 over all files."""
	local('pep8 fabfile.py themelog test')

def clean_py():
	"""Remove *.pyc and *.pyo files.
	"""
	# local("find . -name '*.pyo' -exec rm {} \;
	from unipath import Path
	from unipath import FILES
	cc_pyo = 0
	cc_pyc = 0
	print('Looking for .pyo and .pyc files...')
	for f in Path('themelog').walk(filter=FILES):
		if f.ext == '.pyo':
			f.remove()
			cc_pyo += 1

		if f.ext == '.pyc':
			f.remove()
			cc_pyc += 1

	print('Deleted {o} .pyo and {c} .pyc files'.format(o=cc_pyo, c=cc_pyc))
