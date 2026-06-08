PORT ?= 8000

.PHONY: serve dev

serve:
	uv run tools/wiki_server.py --port $(PORT)

dev:
	uv run tools/wiki_server.py --dev --port $(PORT)
