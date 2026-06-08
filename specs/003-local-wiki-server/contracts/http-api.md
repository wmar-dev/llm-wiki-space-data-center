# HTTP Interface Contract: Local Wiki Server

**Phase 1 output for**: `003-local-wiki-server`
**Date**: 2026-06-07

The local wiki server exposes a minimal HTTP interface on `localhost`. All routes serve read-only content.

---

## Base URL

```
http://localhost:{PORT}
```

Default `PORT` is `8000`. Configurable via the `--port` flag at startup.

---

## Routes

### `GET /`

Returns the rendered HTML of `index.md` from the project root.

| Property | Value |
|----------|-------|
| Response type | `text/html; charset=utf-8` |
| Status (success) | `200 OK` |
| Status (missing) | `404 Not Found` |

---

### `GET /wiki/{path}`

Returns the rendered HTML of the markdown file at `wiki/{path}.md`.

Accepts the path with or without the `.md` extension:
- `GET /wiki/concepts/foo` → serves `wiki/concepts/foo.md`
- `GET /wiki/concepts/foo.md` → same result

If `path` resolves to a directory, returns an auto-generated index listing the `.md` files within it.

| Property | Value |
|----------|-------|
| Response type | `text/html; charset=utf-8` |
| Status (success) | `200 OK` |
| Status (missing file) | `404 Not Found` |
| Status (directory, no index) | `200 OK` with directory listing |

---

### `GET /log.md`

Returns the rendered HTML of `log.md`.

---

### `GET /llm-wiki.md`

Returns the rendered HTML of `llm-wiki.md`.

---

### `GET /__mtime`

Returns the most recent modification timestamp across all served wiki files. Used by the live-reload browser script.

**Response body** (`application/json`):
```json
{ "mtime": 1749312000.0 }
```

| Property | Value |
|----------|-------|
| Response type | `application/json` |
| Status | `200 OK` always |

---

### `GET /**` (all other paths)

Returns HTTP 403 Forbidden with a plain-text body: `Access denied.`

This covers `/specs/`, `/.specify/`, `/raw/`, `/tools/`, and any other path not in the whitelist.

---

## Error Responses

| Status | Condition |
|--------|-----------|
| `400 Bad Request` | Malformed or path-traversal URL (`../` attempts) |
| `403 Forbidden` | Path not in the whitelist |
| `404 Not Found` | Whitelisted path with no corresponding `.md` file |
| `413 Content Too Large` | Source file exceeds 5 MB |

All error responses are `text/plain; charset=utf-8`.

---

## Startup Behaviour

On bind failure (port already in use):
- Prints to stderr: `Error: port {PORT} is already in use. Choose another with --port.`
- Exits with code `1`.

On successful start:
- Prints to stdout: `Wiki server running at http://localhost:{PORT}`
- Prints to stdout: `Press Ctrl+C to stop.`

On shutdown (Ctrl+C / SIGINT):
- Prints to stdout: `Shutting down.`
- Exits with code `0`.
