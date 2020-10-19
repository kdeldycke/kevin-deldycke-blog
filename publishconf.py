#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from importlib.machinery import SourceFileLoader
from pathlib import Path


SourceFileLoader(
    "pelicanconf",
    str(Path(__file__).parent.joinpath("pelicanconf.py").resolve()),
).load_module()


SITEURL = "https://kevin.deldycke.com"
