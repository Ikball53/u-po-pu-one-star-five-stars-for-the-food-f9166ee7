"""One Star, Five Stars for the Food.

Writes a single-sentence alien tourist review of Earth to entry.txt.
The visitor docks Earth one star for leaking skies, rectangle-worshipping
locals and gravity that never says sorry, then admits the noodles alone
were worth the crash landing. Deterministic, stdlib only, no network,
no randomness: the same sentence every run.
"""

import os

REVIEW = (
    "One star: the sky leaks with no refund policy, the locals worship "
    "glowing rectangles, and gravity never apologises \u2014 but the noodles "
    "were worth the crash landing."
)

MAX_CHARS = 200


def pick_output_dir():
    """Return the directory the entry file goes in."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.getcwd(), "output")


def is_single_sentence(text):
    """True when text holds exactly one sentence: one terminal period,
    and no other sentence-ending punctuation anywhere in it."""
    stripped = text.strip()
    if not stripped:
        return False
    if stripped.count(".") != 1:
        return False
    if "!" in stripped or "?" in stripped:
        return False
    return stripped.endswith(".")


def checked_review():
    """Return REVIEW after enforcing the competition gate in code."""
    text = REVIEW.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("review must be 1-200 characters, got %d" % len(text))
    if not is_single_sentence(text):
        raise ValueError("review must be exactly one sentence")
    return text


def main():
    text = checked_review()
    out_dir = pick_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(text.encode("utf-8"))
    print("wrote %d characters to %s" % (len(text), path))


if __name__ == "__main__":
    main()
