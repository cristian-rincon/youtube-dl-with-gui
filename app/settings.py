import enum
from pathlib import Path


class Config(enum.Enum):
    DOWNLOADS_PATH : str = str(Path.home() / "Downloads")
