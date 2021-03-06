#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def download_github_code(path):
    filename = path.rsplit("/")[-1]
    os.system("wget https://raw.githubusercontent.com/hse-aml/natural-language-processing/master/{} -O {}".format(path, filename))


def setup_common():
    os.system("pip install tqdm")
    os.system("pip install backports.weakref==1.0.post1")
    os.system("pip install ChatterBot==0.7.6")
    os.system("pip install enum34==1.1.6")
    os.system("pip install funcsigs==1.0.2")
    os.system("pip install gensim==3.1.0")
    os.system("pip install jedi==0.11.0")
    os.system("pip install libarchive==0.4.4")
    os.system("pip install mock==2.0.0")
    os.system("pip install parso==0.1.0")
    os.system("pip install pbr==3.1.1")
    os.system("pip install regex==2017.11.9")

    download_github_code("common/download_utils.py")
    download_github_code("common/tqdm_utils.py")
    download_github_code("common/__init__.py")
    os.system("mkdir common")
    os.system("mv download_utils.py tqdm_utils.py __init__.py common/")


def setup_week1():
    setup_common()
    download_github_code("week1/grader.py")
    download_github_code("week1/metrics.py")


def setup_week2():
    setup_common()
    download_github_code("week2/evaluation.py")


def setup_week3():
    setup_common()
    download_github_code("week3/grader.py")
    download_github_code("week3/util.py")


def setup_week4():
    setup_common()


def setup_project():
    setup_common()
    download_github_code("project/dialogue_manager.py")
    download_github_code("project/main_bot.py")
    download_github_code("project/utils.py")


def setup_honor():
    setup_common()
    download_github_code("honor/datasets.py")
    download_github_code("honor/example.py")
    download_github_code("honor/download_cornell.sh")
    download_github_code("honor/download_opensubs.sh")
