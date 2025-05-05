"""
Guide module.

Provides lookup functions to query resources by name.
"""

from .resource import Resource

def find_resource_info(name: str, resources: list[Resource]) -> str:
    """
    Search for a resource by name and return its info string.

    Args:
        name (str): The resource to look up (case‑insensitive).
        resources (list[Resource]): Preloaded list of Resource objects.

    Returns:
        str: Description from Resource.get_info() or "Resource not found."
    """
    