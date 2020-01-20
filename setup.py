#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/realestate_cashflow.svg
        :target: https://pypi.python.org/pypi/realestate_cashflow
.. image:: https://img.shields.io/travis/greghor/realestate_cashflow.svg
        :target: https://travis-ci.org/greghor/realestate_cashflow

Compute the basic cashflow associated to a real estate investment


Links:
---------
* `Github <https://github.com/greghor/realestate_cashflow>`_
"""

from setuptools import setup, find_packages

requirements = ['Click>=6.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Gregoire Hornung",
    author_email='greghor4@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Compute the basic cashflow associated to a real estate investment",
    entry_points={
        'console_scripts': [
            'realestate_cashflow=realestate_cashflow.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=__doc__,
    include_package_data=True,
    keywords='realestate_cashflow',
    name='realestate_cashflow',
    packages=find_packages(include=['realestate_cashflow']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/greghor/realestate_cashflow',
    version='0.1.0',
    zip_safe=False,
)
