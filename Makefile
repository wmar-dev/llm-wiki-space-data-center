PORT ?= 8000

.PHONY: serve dev test

serve:
	uv run tools/wiki_server.py --port $(PORT)

dev:
	uv run tools/wiki_server.py --dev --port $(PORT)

test:
	uv run tools/test_wiki_server.py
