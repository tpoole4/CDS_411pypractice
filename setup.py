#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

with open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

name = "cds411_fa18_homework06"
version = "2018.11"
release = "2018.11.13"

setuptools.setup(
    name=name,
    author="James K. Glasbrenner",
    author_email="jglasbr2@gmu.edu",
    license="Creative Commons Attribution-ShareAlike 4.0 International",
    version=release,
    description=("Starter files for CDS 411 Homework 6."),
    long_description=readme,
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=[
        "jupyter == 1.0.0",
        "jupyterlab == 0.34.3",
        "jupyterlab_git",
        "jupyterlab_github",
        "matplotlib == 2.2.3",
        "nb_pdf_template",
        "numpy == 1.15.0",
        "pandas == 0.23.4",
        "scikit-learn == 0.19.1",
        "scipy == 1.1.0",
        "seaborn == 0.9.0",
        "statsmodels == 0.9.0",
        "yapf",
    ],
)
