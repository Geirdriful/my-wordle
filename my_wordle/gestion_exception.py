#! /usr/bin/env python3

class HTTPException(Exception):

    def __init__(self, message, value):
        super().__init__(message, value)
