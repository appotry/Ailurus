#!/usr/bin/env python
import os, sys, glob
from distutils.core import setup
from DistUtilsExtra.command import *

setup(name = 'ailurus',
      description = 'recording installed software, recovering system later',
      version = '12.08',
      maintainer = 'Homer Xing',
      maintainer_email = 'homer.xing@gmail.com',
      url = 'http://ailurus.googlecode.com/',
      license = 'GPLv2+',
      platforms = ['linux'],
      packages = ['ailurus', 'ailurus.support',],
      package_data={'ailurus.support': [os.path.basename(f) for f in glob.glob('ailurus/support/*') if '.' not in os.path.basename(f)],},
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
