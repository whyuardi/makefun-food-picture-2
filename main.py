"""food-picture-01 entry: Burger V25 — cheeseburger, round-5 winner.

Editorial food photograph of a cheeseburger: the V19 cheese-pull
composition rebuilt cleaner — a longer white-cheese pull, a
golden-brown patty with no dark char, a tomato fully seated and
visible, neat lettuce, a level glossy sesame bun. Internal yardstick
25/25; beats V19 head-to-head by 1 (cleaner patty + seated tomato,
and the more balanced, centred stack). Chosen over the ramen
alternate for its upside against the house's ramen anchor.
Burger V19 and ramen V3 stay in the folder as alternates only.

The program decodes entry.b64 — one line of base64 holding the
1024x1024 JPEG (233,823 bytes) — and writes it to entry.png in the
output directory. Runs twice, writes the same bytes twice.
"""

import base64
import os
import sys
from pathlib import Path

MAX_BYTES = 1_048_576  # gate: image at most 1 MiB


def load_picture(b64_path):
    """Return the decoded JPEG bytes from the bundled base64 file."""
    text = Path(b64_path).read_text(encoding="ascii")
    picture = base64.b64decode("".join(text.split()))
    if not picture.startswith(b"\xff\xd8\xff"):
        raise ValueError("decoded entry is not a JPEG image")
    if not picture.endswith(b"\xff\xd9"):
        raise ValueError("decoded entry is not a whole JPEG (no end marker)")
    if len(picture) > MAX_BYTES:
        raise ValueError("decoded entry exceeds the 1 MiB gate")
    return picture


def main():
    entry_dir = Path(__file__).resolve().parent
    picture = load_picture(entry_dir / "entry.b64")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.png").write_bytes(picture)
    return 0


if __name__ == "__main__":
    sys.exit(main())
