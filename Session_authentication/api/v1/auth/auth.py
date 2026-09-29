#!/usr/bin/env python3
""" Auth module
"""
from os import getenv
from typing import List, TypeVar
from flask import request


class Auth:
    """ Auth class: template for all authentication systems
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determine if a path requires authentication
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        slash_tolerant_path = path if path.endswith('/') else path + '/'
        for excluded_path in excluded_paths:
            if excluded_path == slash_tolerant_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Return the value of the request's Authorization header
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return the current authenticated user for the request
        """
        return None

    def session_cookie(self, request=None):
        """ Return the value of the session cookie from a request
        """
        if request is None:
            return None
        session_name = getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(session_name)
