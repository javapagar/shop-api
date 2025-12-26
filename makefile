.PHONY: api-dev

api-dev:
	uv run uvicorn main:app --reload