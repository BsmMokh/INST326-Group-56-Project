"""
Data loader module.

Parses the JSON file of resource definitions and returns
a list of Resource objects.
"""

import json
from .resource import Resource

def load_resources(path: str) -> list[Resource]:
    """
    Load resource data from a JSON file and return Resource instances.

    Args:
        path (str): Filesystem path to resources.json.

    Returns:
        list[Resource]: List of resources defined in the file.

    Raises:
        FileNotFoundError: If the file is not found.
        ValueError: If JSON is malformed or missing fields.
    """
    # implementation goes here
