from dataclasses import dataclass
from pathlib import Path

from .base_theme import Theme

@dataclass
class GoldenPear(Theme):
    """Golden Pear theme extending the base Theme class

    Overwrite all desired attributers or methods.
    """

    # Here I only overwrite the palette file path, as by default it will be used,
    # however I could instead simply overwrite the colors directly here and not
    # load from JSON
    palette: Path = "themes/example_theme.json"
