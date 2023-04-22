init:
	pyenv install 3.8.2
	pyenv local 3.8.2
	pyenv exec pip install poetry
	pyenv exec poetry install

run:
	pyenv exec poetry run python
