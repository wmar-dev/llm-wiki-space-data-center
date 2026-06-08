# Space Data Center Prospects Analysis Wiki

An LLM-maintained wiki analyzing space data center prospects, built using the [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#file-llm-wiki-md) pattern by Andrej Karpathy.

---

See [SUMMARY.md](SUMMARY.md) for the current viability assessment.

---

## Browsing Locally

Requires [uv](https://docs.astral.sh/uv/).

```bash
make serve          # http://localhost:8000
make dev            # same, with live reload on file changes
PORT=9000 make serve  # custom port
```

`make dev` also auto-restarts the server when `tools/wiki_server.py` itself changes.
