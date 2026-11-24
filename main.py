"""Loading Screen Gold: a tip in 200 characters.

Writes a single loading-screen tip (1-200 chars, one line, no trailing
newline) to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Stdlib only, deterministic.
"""

import os
import tempfile

TIP = (
    "Tip: your agent read every file, including the one named "
    "final_final_v2. It hasn't judged you yet. Breathe."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(TIP)
        os.chmod(tmp, 0o644)
        os.replace(tmp, target)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
