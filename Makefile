venv:
	@echo "Setting up python environment.."
	@python3 -m venv .venv && \
	. ./.venv/bin/activate && \
	pip install --quiet --upgrade pip && \
	pip install --quiet -r requirements.txt

run: venv
	@./.venv/bin/python main.py