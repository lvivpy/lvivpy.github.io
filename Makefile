dummy:
	echo ""

bootstrap:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

build:
	. .venv/bin/activate && $(MAKE) -C src html
