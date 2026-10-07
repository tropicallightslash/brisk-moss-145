"""Quick sanity check for a local checkout."""

import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    required = ["assets", "docs", "scripts", "tests"]
    missing = [d for d in required if not (root / d).is_dir()]
    if missing:
        print("missing:", ", ".join(missing))
        return 1
    print("layout OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
