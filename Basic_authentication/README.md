# Basic authentication

## Description
This project implements Basic Authentication on a simple Flask API, step by
step, to understand the mechanism itself (in production you'd use a library
like Flask-HTTPAuth instead of hand-rolling this).

## Resources
- [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY)
- [Base64 in Python](https://docs.python.org/3.7/library/base64.html)
- [HTTP header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
- [Flask](https://flask.palletsprojects.com/)
- [Base64 - concept](https://en.wikipedia.org/wiki/Base64)

## Learning Objectives
By the end of this project, you should be able to explain, without Google:
- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

## Requirements
- All files interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/env python3`
- Code follows the `pycodestyle` style (version 2.5)
- All files are executable
- All modules, classes, and functions are documented with real, explanatory docstrings

## Setup and start server
```
pip3 install -r requirements.txt
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```
Set `AUTH_TYPE=auth` for the base `Auth` class, or `AUTH_TYPE=basic_auth` for full Basic Authentication.

## Tasks
| File | Description |
| --- | --- |
| `api/v1/app.py` | Flask app entrypoint: error handlers (404/401/403), `auth` instance selection via `AUTH_TYPE`, and the `before_request` filter |
| `api/v1/views/index.py` | `/status`, `/stats`, `/unauthorized`, and `/forbidden` endpoints |
| `api/v1/auth/auth.py` | `Auth` base class: `require_auth`, `authorization_header`, `current_user` |
| `api/v1/auth/basic_auth.py` | `BasicAuth`: Base64 extraction/decoding, credential parsing, and user lookup |
| `models/` | `Base` and `User` models with file-based (de)serialization |
