"""Write the entry image to the output directory.

The image ships in this repository as entry.png.b64 (base64 text): this
program decodes it and writes the exact bytes to
<MAKEFUN_OUTPUT_DIR>/entry.png. Standard library only, no network, and
deterministic: the same input bytes produce the same output bytes on
every run. The decoded bytes are checked to be a whole PNG (its 8-byte
signature) before anything is written, so a corrupt payload fails loudly
instead of producing a broken entry. The decoded size and the IHDR
dimensions are also checked (at most 1 MiB, at most 1024x1024) before
anything is written.
"""

import base64
import os
import struct
import sys

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576
MAX_DIMENSION = 1024


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.png.b64"), "r", encoding="ascii") as f:
        data = base64.b64decode(f.read())
    if data[:8] != PNG_SIGNATURE:
        print("entry.png.b64 does not decode to a PNG", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(
            f"entry.png.b64 decodes to {len(data)} bytes, over the 1 MiB limit",
            file=sys.stderr,
        )
        return 1
    if len(data) < 24 or data[12:16] != b"IHDR":
        print("entry.png.b64 decodes to a truncated PNG (no IHDR)", file=sys.stderr)
        return 1
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        print(
            f"entry.png is {width}x{height}, larger than the "
            f"{MAX_DIMENSION}x{MAX_DIMENSION} limit",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.png"), "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
