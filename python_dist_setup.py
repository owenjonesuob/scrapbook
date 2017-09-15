### Set up a Python DISTRIBUTION (possibly multiple packages!)

# Use setuptools.setup because it's easy and everyone does
from setuptools import setup

setup(
    name="distname", # name of the distribution
    version="0.1.0", # use semantic versioning
    packages=["pkg1", "pkg2"], # you can install more than one package with your distribution
    package_data={
        "pkg1": ["non_py_file1.txt", "non_py_file2.json"],
        "pkg1": ["non_py_file3.txt", "non_py_file4.json"] # if you have non-py files (e.g. data files) include them like this
    }
)