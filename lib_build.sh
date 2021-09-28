#!/bin/sh
# cd C:\\Users\\Ramesh\\Documents\\exceltotxt\\excel_to_txt_convertor_package
# pip uninstall excel_to_txt_convertor-0.1-py3-none-any.whl
python setup.py sdist bdist_wheel
twine upload --verbose -u raosamrudhi@gmail.com -p AP2696VZzk1SBBXqbcMQJfV2qti --repository-url https://samrudhi.jfrog.io/artifactory/api/pypi/default-pypi-local dist/*
# cd dist
# pip install excel_to_txt_convertor-0.1-py3-none-any.whl
