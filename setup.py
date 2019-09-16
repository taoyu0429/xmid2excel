#!/usr/env/bin python
# -*- coding: utf-8 -*-
import io
import os
import sys
import setuptools

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'xmind2xls', '__about__.py'), encoding='utf-8') as f:  # custom
    exec(f.read(), about)

with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

install_requires = [  # custom
    "xmind",
    "openpyxl",
]

setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=setuptools.find_packages(exclude=['xmind.*', 'docs']),  # custom
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    python_requires='>=3.0, <4',  # custom

    entry_points={  # custom
        'console_scripts': [
            'xmind2xls=xmind2xls.cli:cli_main',
        ]
    }

)

