#!/usr/local/bin/python3

class BirchReturn(Exception):
    def __init__(self, value):
        self.value = value
