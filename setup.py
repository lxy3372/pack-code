#!/usr/bin/env python

import py2exe
from distutils.core import setup

options = {"py2exe":{"compressed": 1, "optimize": 2, "bundle_files": 1, "dll_excludes": []}}
data_files = [("bitmaps", ["./bitmaps/zip.ico"])]
setup(windows=["wxrun.py"], options=options, zipfile=None, data_files=data_files, requires=['wx'])