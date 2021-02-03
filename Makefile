.PHONY: install
install:
	pip3 install -r requirements.txt

.PHONY: run
run:
	flask run
