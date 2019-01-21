#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


import os
import codecs

def read(filename):
    return codecs.open(filename, encoding='utf-8').read()


long_description = '\n\n'.join([read('README'),
                                read('AUTHORS'),
                                read('CHANGES')])

__doc__ = long_description

root_folder = os.path.dirname(os.path.abspath(__file__))

setup(name='lantz-sims',
      version='0.5.2',
      license='BSD',
      description='Instrumentation framework',
      long_description=long_description,
      keywords='measurement control instrumentation science',
      author='Hernan E. Grecco',
      author_email='hernan.grecco@gmail.com',
      url='https://github.com/lantzproject',
      install_requires=['lantz-core>=0.5',
                        ],
      packages=['lantz.sims'],
      zip_safe=False,
      platforms='any',
      entry_points={
          'console_scripts': [
              'lantz-sims = lantz.sims.__main__:main'
          ],
          'lantz_subcommands': [
              'sims = lantz.sims.__main__:main'
          ]
      },
      classifiers=[
           'Development Status :: 4 - Beta',
           'Intended Audience :: Developers',
           'Intended Audience :: Science/Research',
           'License :: OSI Approved :: BSD License',
           'Operating System :: MacOS :: MacOS X',
           'Operating System :: Microsoft :: Windows',
           'Operating System :: POSIX',
           'Programming Language :: Python',
           'Programming Language :: Python :: 3.6',
           'Topic :: Scientific/Engineering',
           'Topic :: Software Development :: Libraries'
      ],
)
