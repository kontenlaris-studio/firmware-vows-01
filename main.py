"""Till Firmware Do Us Part entry: wedding vows in patches and rollbacks."""

import os

JOKE = (
    "Till firmware do us part: I will patch your worst days, roll back my "
    "worst moods, and never, ever leave you stuck on 99 percent."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(f"wrote {path} ({len(JOKE)} characters)")


if __name__ == "__main__":
    main()
