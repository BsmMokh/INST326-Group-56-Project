"""
Resource definition module.

Contains a `Resource` class representing a Minecraft resource
and its gathering metadata.
"""

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
    def __init__(self, name: str, location: str, depth_range: tuple[int,int],
                 required_tool: str, method: str):
        """Initialize a Resource instance."""
        self.name = name
        self.location = location
        self.depth_range = depth_range
        self.required_tool = required_tool
        self.method = method

    def get_info(self) -> str:
        """
        Return a user‑friendly description of how and where to find this resource.
        """

