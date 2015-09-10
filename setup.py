from __future__ import print_function

from setuptools import setup  # , find_packages
import io
import os
# import sys

# import ggpio

here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding):
            buf.append(filename.read())
    return sep.join(buf)

long_desc = read('README', 'CHANGES', 'TODO')

setup(
    description='',
    author='Konstantin Schukraft',
    url='',
    download_url='',
    author_email='konstantin@schukraft.org',
    version='',
    install_requires=[],
    packages=[],
    scripts=[],
    name='',
    license='',
    long_description=long_desc,
    test_suite='test.test_sandman',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    extras_require={}
)
