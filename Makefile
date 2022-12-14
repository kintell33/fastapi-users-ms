install: venv/bin/activate
ifdef pkg
	./venv/bin/pip install $(pkg)
	./venv/bin/pip freeze > requirements.txt
else
	@echo 'no pkg defined, please execute make pkg=package_to_install install'
endif

freeze:
	./venv/bin/pip freeze > requirements.txt
run: venv/bin/activate
	./venv/bin/uvicorn main:app --reload
clean:
	rm -rf __pycache__
	rm -rf venv
	rm -rf .pytest_cache
venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
test: venv/bin/activate
	@echo  "\033[33m ========= TESTS =========== \033[0m"
	@echo "\n"
	./venv/bin/coverage run -m pytest tests
	@echo "\n"
	@echo  "\033[33m ========= COVERAGE =========== \033[0m"
	
	./venv/bin/coverage report