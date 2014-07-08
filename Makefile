lint:
	flake8 --exclude=_version.py pinch/

test:
	python -mtesttools.run discover
