# User authentication service

## Description
This project builds a full email/password authentication service from
scratch on top of Flask and SQLAlchemy: a `User` model, a `DB` storage
layer, an `Auth` business-logic layer, and a Flask app exposing
registration, login/logout (session-cookie based), a profile endpoint, and
a password-reset flow.

## Resources
- [Flask documentation](https://flask.palletsprojects.com/)
- [Requests module](https://requests.readthedocs.io/)
- [HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## Learning Objectives
By the end of this project, you should be able to explain, without Google:
- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

## Requirements
- All files interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/env python3`
- Code follows the `pycodestyle` style (version 2.5)
- All files are executable
- All modules, classes, and functions are documented with real, explanatory docstrings
- All functions are type-annotated
- The Flask app only ever talks to `Auth`, never to `DB` directly; only public methods of `Auth` and `DB` are used outside those classes

## Setup
```
pip3 install -r requirements.txt
python3 app.py
```

## Tasks
| File | Description |
| --- | --- |
| `user.py` | `User` SQLAlchemy model for the `users` table |
| `db.py` | `DB` class: `add_user`, `find_user_by`, `update_user` |
| `auth.py` | `Auth` class: register, login validation, sessions, and password reset, backed by `_hash_password`/`_generate_uuid` |
| `app.py` | Flask routes: `/`, `/users`, `/sessions`, `/profile`, `/reset_password` |
