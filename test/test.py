#!/usr/bin/env python3
# encoding: utf-8
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'packagemanager'))
from packagemanager import *

App = packagemanager()
App.install('nginx', 'rsync')
