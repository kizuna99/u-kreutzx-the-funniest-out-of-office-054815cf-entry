# SPDX-License-Identifier: MIT
"""Write the out-of-office entry line to /output/entry.txt."""
import os

TEXT = (
    "I'm away until Monday. My work phone came along by mistake, so your "
    "email and I are by the sea, politely ignoring each other."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
