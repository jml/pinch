# Copyright (c) Jonathan M. Lange
# See LICENSE for details.

from os import path

from setuptools import setup

import versioneer
versioneer.versionfile_source = 'pinch/_version.py'
versioneer.versionfile_build = 'pinch/_version.py'
versioneer.tag_prefix = '' # tags are like 1.2.0
versioneer.parentdir_prefix = 'pinch-' # dirname like 'myproject-1.2.0'



def read(path):
    """
    Read the contents of a file.
    """
    with open(path) as f:
        return f.read()



if __name__ == '__main__':
    setup(
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'License :: OSI Approved :: Apache License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: Implementation :: CPython',
            'Programming Language :: Python :: Implementation :: PyPy',
        ],
        name='pinch',
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        description=(
            'todo.txt command-line interface.'),
        install_requires=[],
        keywords='release',
        license='Apache',
        packages=['pinch', 'pinch.tests'],
        url='https://github.com/jml/pinch',
        maintainer='Jonathan M. Lange',
        maintainer_email='jml@mumak.net',
        long_description=read(path.join(path.dirname(__file__), "README.md")),
    )
