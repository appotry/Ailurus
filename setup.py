#!/usr/bin/env python
import os, sys, glob
from distutils.core import setup
from DistUtilsExtra.command import *

setup(name = 'ailurus',
      description = 'backup a name list of installed software',
      version = '12.08',
      maintainer = 'Homer Hsing',
      maintainer_email = 'homer.hsing@gmail.com',
      url = 'http://ailurus.googlecode.com/',
      license = 'GPLv2+',
      platforms = ['linux'],
      packages = ['ailurus'],
      data_files = [
        ('share/man/man1/', ['ailurus.1']),
        ('share/applications/', ['ailurus.desktop']),
      ],
      scripts = ['bin/ailurus'],
      cmdclass = { 'build' :  build_extra.build_extra,
                   'build_i18n' :  build_i18n.build_i18n,
                   'build_help' :  build_help.build_help,
                   'build_icons' :  build_icons.build_icons
                 }
      )
