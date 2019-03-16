#!/usr/bin/env python3
# encoding: utf-8
import os
import sys
import distro

class packagemanager(object):
	_distro = '' # tuble.  info about OS distribution.
	_packagemanager = '' # package manager
	_cmd_install = '' # command instructs for installing

	def __init__(self):
		self._distro = distro.linux_distribution(full_distribution_name=False)
		if "debian" in self._distro[0].lower():
			self._packagemanager = 'apt-get'
			self._cmd_install = self._packagemanager+' -qq install '
		elif "ubuntu" in self._distro[0]:
			self._packagemanager = 'apt-get'
		elif "centos" in self._distro[0]:
			self._packagemanager = 'yum'
		elif "fedora" in self._distro[0]:
			if  int(self._distro[1]) >= 22:
				self._packagemanager = 'dnf' # dnf defualt since fedora 22
			else:
				self._packagemanager = 'yum'
		else:
			raise ValueError("\nFailed to detect PackageManager for OS "+self._distro[0]+" "+self._distro[1])

	def get_packagemanager(self):
		return self._packagemanager

	def install(self, *args):
		if self._packagemanager == 'apt-get': # debian
			cmd = self._packagemanager+' -qq install '
		elif self._packagemanager == 'yum': # centos
			cmd = self._packagemanager+' -y -q install '
		else:
			cmd = self._packagemanager+' install '+' '.join(args[1:])
		print('command '+cmd)
		os.system(cmd)

'''
Should not be exec as CLI
Only to be imported in python projects
'''
if __name__ == "__main__":
	pass
