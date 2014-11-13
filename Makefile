.PHONY: dev install test cover docs

PYTHON=`which python`
PIP=`which pip`
NOSE=`which nosetests`

install:
	${PYTHON} setup.py install

check:
	${NOSE} --with-doctest barcode

cover:
	${NOSE} --with-coverage --cover-html --cover-erase --cover-package=barcode

docs:
	make -C docs -e PYTHONPATH=".." html
