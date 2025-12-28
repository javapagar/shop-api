.PHONY: api-dev test

test:
	uv run pytest -v
api-dev:
	uv run uvicorn main:app --reload