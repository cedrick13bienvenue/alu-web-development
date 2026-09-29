# Session authentication

## Description
This project implements Session Authentication on top of the Basic
Authentication API from the previous project: a login/logout flow based on
a Session ID stored in a cookie, without installing any extra module.

## Resources
- [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY) - session auth part only
- [HTTP Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
- [Flask](https://flask.palletsprojects.com/)
- [Flask Cookie](https://flask.palletsprojects.com/en/1.1.x/quickstart/#cookies)

## Learning Objectives
By the end of this project, you should be able to explain, without Google:
- What authentication means
- What session authentication means
- What Cookies are
- How to send Cookies
- How to parse Cookies

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
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
```

## Tasks
| File | Description |
| --- | --- |
| `models/`, `api/v1/auth/basic_auth.py`, `api/v1/views/*` | Carried over from `Basic_authentication`, plus a `GET /api/v1/users/me` shortcut for the authenticated user |
| `api/v1/auth/auth.py` | Adds `session_cookie` for reading the session ID cookie from a request |
| `api/v1/auth/session_auth.py` | `SessionAuth`: create/lookup/destroy an in-memory Session ID <-> User ID mapping |
| `api/v1/views/session_auth.py` | `POST /auth_session/login` and `DELETE /auth_session/logout` |
| `api/v1/app.py` | Selects `SessionAuth` via `AUTH_TYPE=session_auth`, exposes `request.current_user`, and accepts either an Authorization header or a session cookie |
