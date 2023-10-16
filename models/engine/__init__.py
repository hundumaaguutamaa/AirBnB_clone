#!/usr/bin/python3
"""Module that defines common attributes fo classes."""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
