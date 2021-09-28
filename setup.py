import os
import setuptools
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
# def read(fname):
#     return open(os.path.join(os.path.dirname(__file__), fname)).read()
REQ = list()
with open ("requirements.txt") as requirements:

    for requirement in requirements.readlines():

        REQ.append(requirement)

setup(
    name = "excel_to_txt_convertor",
    version = "0.1",
    author = "Samrudhi R Rao",
    author_email = "raosamrudhi@gmail.com",
    description = ("An demonstration of how to create, document, and publish "
                                   "to the cheese shop a5 pypi.org."),
    license = "BSD",
    keywords = "example documentation tutorial",
    url = "https://github.com/SamrudhiRRao/ExceltoTxtConvertor",
    packages=['excel_to_txt_convertor_utility','excel_to_txt_convertor_utility/utils'],
    python_requires =">=3.8",
    install_requirements = REQ,
    entry_points = {'console_scripts': ['convert_excel_to_txt = excel_to_txt_convertor_utility.convertdf:main']}
)