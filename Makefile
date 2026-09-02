install:
		uv sync

build:
		uv build

lint:
		uv run ruff check .

project:
		uv run project