.PHONY: all clean ruff test 

# Default target
all: ruff test clean

# Clean temporary and generated files
clean:
	find . \( -type f -name '*.pyc' -or -type d -name '__pycache__' \) -delete
	find . \( -type d -name '.eggs' -or -type d -name '*.egg-info' -or -type d -name '.pytest_cache' \) | xargs rm -rf

ruff:
	ruff check .

test:
	python3 -m pytest
