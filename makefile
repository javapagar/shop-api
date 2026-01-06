.PHONY: api-dev test kill

test:
	uv run pytest -v
api-dev:
	uv run uvicorn main:app --reload
kill:
	pkill -f uvicorn
