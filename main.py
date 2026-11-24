#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one sentence, a wedding vow spoken by a robot at its own
wedding, to /output/entry.txt.
"""

VOW = (
    "I promise to love you through every firmware update, every "
    "low-battery warning, and every reboot, until the day my circuits "
    "go quiet."
)


def validate(vow):
    """Check the vow is exactly one sentence of 1-200 characters."""
    if not vow or not vow.strip():
        raise ValueError("vow is empty or only whitespace")
    if len(vow) > 200:
        raise ValueError("vow is %d characters, over the 200 limit" % len(vow))
    if "\n" in vow or "\r" in vow:
        raise ValueError("vow must be a single line")
    terminators = [c for c in vow if c in ".!?"]
    if len(terminators) != 1:
        raise ValueError("vow must contain exactly one sentence terminator")
    if terminators[0] != vow[-1]:
        raise ValueError("the single terminator must be the final character")
    return True


def main():
    validate(VOW)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == VOW, "read-back mismatch"
    print("Vow: %s" % VOW)
    print("Characters: %d" % len(VOW))


if __name__ == "__main__":
    main()
