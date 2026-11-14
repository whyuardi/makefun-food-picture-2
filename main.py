"""Food picture entry — writes the baked-in photograph to /output/entry.png.

The photograph travels as base64 text in entry.b64 next to this file.
"""

import base64
from pathlib import Path

HERE = Path(__file__).resolve().parent
DESTINATION = Path("/output/entry.png")


def write_picture() -> Path:
    encoded = (HERE / "entry.b64").read_text(encoding="ascii").strip()
    picture = base64.b64decode(encoded)
    if not picture.startswith(b"\xff\xd8"):
        raise ValueError("entry.b64 does not decode to a JPEG picture")
    DESTINATION.parent.mkdir(exist_ok=True)
    DESTINATION.write_bytes(picture)
    return DESTINATION


if __name__ == "__main__":
    write_picture()
