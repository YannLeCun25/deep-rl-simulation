install:
	pip install -r requirements.txt

test:
	pytest tests/

run:
	python src/main.py

lint:
	flake8 .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
