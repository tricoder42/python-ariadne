# coding: utf-8
from __future__ import unicode_literals

import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import ariadne


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        sys.exit(pytest.main(self.test_args))

setup(
    name='ariadne',
    version=ariadne.__version__,
    license='MIT',

    author='Tomáš Ehrlich',
    author_email='tomas.ehrlich@gmail.com',

    description="Functional/integration testing for websites",
    long_description=open('README.md').read(),
    url='https://github.com/tricoder42/python-ariadne',

    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=1.4',
        'attrdict==2.0.0',
    ],

    cmdclass={'test': PyTest},
    tests_require=[
        'mock',
        'pytest',
        'pytest-splinter',
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
