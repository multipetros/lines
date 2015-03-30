from distutils.core import setup
import py2exe, sys, os

setup(
    console=[{
        "script":"lines.py",
    }],
    options = {
        "py2exe": {
            "bundle_files": 1,
            "optimize": 2,
            "compressed": 1,
            "ascii": False,
        }
    },
    data_files=["README.md","LICENSE",],
    zipfile = None,
    #zipfile = "python.lib",
    version = "1.0",
    name = "lines",
    description = "A line numbering program for text files",
    author = "Petros Kyladitis",
    author_email ="petros.kyladitis@gmail.com",
    license = "GNU GPL 3 Licence",
    url = "http://www.multipetros.gr",
    )
