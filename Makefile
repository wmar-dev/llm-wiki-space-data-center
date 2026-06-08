PORT ?= 8000

.PHONY: serve

serve:
	uv run tools/wiki_server.py --port $(PORT)
