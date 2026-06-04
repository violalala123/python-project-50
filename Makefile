install:
	uv sync
test:
	uv run pytest
lint:
	uv run ruff check .
test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml