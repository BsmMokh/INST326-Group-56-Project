"""
Minecraft Resource Guide

A program that helps players find information about Minecraft resources,
including where to find them and what tools are needed to obtain them.
"""

import csv

class Resource:
    """
    A Minecraft resource with metadata on where and how to obtain it.

    Attributes:
        name (str): The resource name (e.g., "Diamond").
        location (str): Biome or dimension (e.g., "Overworld").
        depth_range (tuple[int,int]): Min/max Y-levels where it spawns.
        required_tool (str): Minimum tool tier needed (e.g., "Iron Pickaxe").
        method (str): How to obtain (e.g., "Mining", "Smelting").
    """
    def __init__(self, name: str, location: str, depth_range: tuple[int,int],required_tool: str, method: str):
        """Initialize a Resource instance."""
        self.name = name
        self.location = location
        self.depth_range = depth_range
        self.required_tool = required_tool
        self.method = method

    def get_info(self) -> str:
        """
        Return a user‑friendly description of how and where to find this resource.
        
        Returns:
            str: A formatted string containing the resource information
        """
        return (f"{self.name} can be found in the {self.location} "
                f"between Y-levels {self.depth_range[0]} and {self.depth_range[1]}. "
                f"It requires a {self.required_tool} and can be obtained by {self.method}.")

def find_resource_info(name: str, resources: list[Resource]) -> str:
    """
    Search for a resource by name and return its info string.
    Also supports loose matching (the user can input diamond that matches with Diamond Ore)

    Args:
        name (str): The resource to look up (case‑insensitive).
        resources (list[Resource]): Preloaded list of Resource objects.

    Returns:
        str: Description from Resource.get_info() or "Resource not found."
    """
    #Convert the input to lowercase and remove any "ore" suffix
    search_name = name.lower().replace(" ore", "")

    for resource in resources:
        if resource.name.lower() == name.lower():
            return resource.get_info()
        
    matches = []
    for resource in resources:
        resource_name = resource.name.lower().replace(" ore", "")
        if search_name in resource_name:
            matches.append(resource)
    
    if len(matches) == 1:
        return matches[0].get_info()
    elif len(matches) > 1:
        return("Multiple resources found: Be more specific")

    return "Resource not found."


def load_resources(path: str) -> list[Resource]:
    """
    Load resource data from a CSV file and return Resource instances.

    Args:
        path (str): Filesystem path to resources.csv.

    Returns:
        list[Resource]: List of resources defined in the file.

    Raises:
        FileNotFoundError: If the file is not found.
        ValueError: If CSV is malformed or missing fields.
    """
    resources = []
    try:
        with open(path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    # Convert Y Level to a depth range (using ±5 levels around the given Y)
                    y_level = int(row['Y Level'])
                    depth_range = (y_level - 5, y_level + 5)
                    
                    resource = Resource(
                        name=row['Ore Name'],
                        location=row['Dimension'],
                        depth_range=depth_range,
                        required_tool=row['Required Pickaxe'],
                        method="Mining"  # All ores are obtained by mining
                    )
                    resources.append(resource)
                except (KeyError, ValueError) as e:
                    raise ValueError(f"Invalid data format in CSV: {str(e)}")
    except FileNotFoundError:
        raise FileNotFoundError(f"Resource file not found: {path}")
    
    return resources 