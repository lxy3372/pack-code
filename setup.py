#!/usr/bin/env python

import py2exe
from distutils.core import setup

options = {"py2exe":{"compressed": 1, "optimize": 2, "bundle_files": 1}}
setup(service=["run.py"], options=options, zipfile=None)