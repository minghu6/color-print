"""Setup file"""
import os
import re
import codecs
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

def find_version():
    here = os.path.abspath(os.path.dirname(__file__))
    there = os.path.join(here, '__init__.py')

    version_file = codecs.open(there, 'r').read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)

    else:
        raise RuntimeError("Unable to find version string.")

__version__ = find_version()

setup(
    name='color_print',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A color print wrapper',
    long_description=README,
    url='https://github.com/minghu6/color_print',
    author='minghu6',
    author_email='a19678zy@163.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
