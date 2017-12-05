all:
	@echo "Comandos disponibles:"
	@echo ""
	@echo "   completar ..."
	@echo ""

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	venv/bin/pip install -Ur requirements.txt
	touch venv/bin/activate

test: venv
	venv/bin/python backend/manage.py test
