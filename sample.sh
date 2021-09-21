#!/bin/sh
cd C:\\Users\\Ramesh\\Documents\\exceltotxt\\excel_to_txt_convertor_package
pip uninstall excel_to_txt_convertor-0.1-py3-none-any.whl
python setup.py sdist bdist_wheel
cd dist
pip install excel_to_txt_convertor-0.1-py3-none-any.whl
