#!/usr/bin/env python

import contextlib
import os

"""
distutils/setuptools install script.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from setuptools import find_packages

# standard package doesn't start with these (we just limit to git for now)
gits = ["git@", "git+ssh"]

def get_package_list(packages):
    std_ps = []
    git_ps = []
    for p in packages:
        for g in gits:
            if p.startswith(g):
                git_ps.append(p)
                break
        std_ps.append(p)
    return std_ps, git_ps

def read_requirements_txt(file_name):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    rq_file = os.path.join(current_dir, file_name)
    with open(rq_file, "r") as f:
        flines = f.readlines()
    return [l for l in flines if l and not l.startswith("#")]

std_ps = []
git_ps = []
for rf in [read_requirements_txt("requirements/core.txt"),
           read_requirements_txt("requirements/tests.txt")]:
    _std_ps, _git_ps = get_package_list(rf)
    std_ps += _std_ps
    _git_ps += git_ps

setup(
    name="take_your_medicine",
    version="0.1",
    description="Check if name taken",
    author="Yeuk Hon Wong",
    author_email="yeukhon.tech@gmail.com",
    packages=find_packages(exclude=["tests*"]),
    install_requires=std_ps,
    dependency_links=git_ps
)
