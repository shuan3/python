SHELL = /bin/bash
venv/bin/activate:
	python3 -m venv venv
	chmod +x venv/bin/activate
	. ./venv/bin/activate && pip install -r requirements.txt
venv:venv/bin/activate
	. ./venv/bin/activate && pip install -r requirements.txt
init:venv
	. ./venv/bin/activate && python3 -m pip install --upgrade pip
