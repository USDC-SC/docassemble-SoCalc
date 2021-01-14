import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.SoCalc',
      version='1.0.0',
      description=('Scheduling Order Document Maker'),
      long_description='Scheduling Order Calcualtor\r\n1.0.0\r\n-renamed docx files for a consistent naming convention\r\n\r\nScheduling Order Calcualtor\r\n- RMG-sched\r\n- BHH-sched\r\n- DCN-sched\r\n- MBS-sched\r\n- default\r\n\r\n0.0.5 \r\n  -Updated URL Terms from So-Calc Application\r\n  \r\n0.0.6\r\n  -Ben recommendation for Reconsider variable be set\r\n  -include file adds all the backup questions to the document\r\n  -include file for Variable declaration\r\n  \r\n0.08\r\n  -Changed Variable names to be easier to understand in future documents\r\n  0.081\r\n    -added MGL, MGB, and PJG\r\n  0.082\r\n    -added JMS, SAL, TLW, TMC\r\n  0.083\r\n    - add DCC, CMC, HMA, JFA, MGL-trial, more PJG, RBH, TLW, SAL-trial\r\n    - KFM files created but will not be uploaded\r\n  0.084 \r\n    -add Magistrates: PJG, SVH, MGB, KDW, TER\r\n    -added JDA\r\n  0.085\r\n    -add ProSe for SVH\r\n    -add ProSe-MBS for PJG\r\n  0.086\r\n    -added SO for MHC',
      long_description_content_type='text/markdown',
      author='Anthony Matrejek',
      author_email='anthony_matrejek@scd.uscourts.gov',
      license='The MIT License (MIT)',
      url='SoCalc',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/SoCalc/', package='docassemble.SoCalc'),
     )

