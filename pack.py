from distutils.core import setup
import py2exe
import sys
import os
import glob
#this allows to run it with a simple double click.
sys.argv.append('py2exe')
 
py2exe_options = {
        "includes": ["sip"],
        "dll_excludes": ["MSVCP90.dll",],
        "compressed": 0,
        "optimize": 2,
        "ascii": 0,
        "bundle_files": 1,
        }
 
setup(
      name = 'ImageCut 1.0',
      author='zhanxianbo',
      version = '1.1',
      windows = ['imageCut.py',], 
      zipfile = None,
      options = {'py2exe': py2exe_options},
      )
