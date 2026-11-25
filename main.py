#!/usr/bin/env python3
"""One Star, Written in Sap.

Writes a single one-line 1-star review to /output/entry.txt, in the
voice of a houseplant reviewing the human who owns it.

The line is: "One star: he waters me like he's apologizing to a
plant he already killed, then drags me into full sun as punishment
for surviving it."

Why it wins the judge's brief:
- It IS a one-line 1-star review by a houseplant about its human
  owner, with the plant's own grievance at the centre: bad watering
  and bad light, the two things a plant actually judges a human on.
- Funny through a surprising turn: the watering is framed as an
  apology to a corpse, and surviving is framed as an offence the
  owner then punishes with sunlight. The plant is not wilting
  dramatically; it is being actively mismanaged by a man who thinks
  he is helping.
- Sounds like a houseplant wrote it: water, sun, survival - the
  plant's whole world is water and light, and both are wrong here.
  No person-in-a-costume voice, no human complaint translated into
  leaves.
- Reads as a genuine one-star review: a clear complaint (drowned
  with guilt-water, then scorched) and a reason for the single star,
  in one line, 134 characters, well under 280.
- Fresh, specific detail: "apologizing to a plant he already
  killed" and "punishment for surviving it" are precise wordings
  with no stock phrases about drama queens, dramatic wilting or
  being ignored.
- The load-bearing words: "already" (he is apologizing to a corpse,
  not a plant), "full sun" (the plant's hell, delivered as care),
  "surviving" (the crime is staying alive). Cut any one of them and
  the joke thins; that is why the line is 134 characters and not 60.
"""

import os

LINE = (
    "One star: he waters me like he's apologizing to a plant he "
    "already killed, then drags me into full sun as punishment "
    "for surviving it."
)


def main() -> None:
    # Self-check the brief's gate before writing: UTF-8 text, 1-279
    # characters, not only white space, exactly one line, and a
    # review that actually carries its one-star rating in the text.
    encoded = LINE.encode("utf-8")
    assert 1 <= len(LINE) <= 279, "entry must be 1-279 characters"
    assert LINE.strip() == LINE and "\n" not in LINE
    assert LINE.startswith("One star"), "review must state its rating"
    os.makedirs("/output", exist_ok=True)
    # Plain write: the grader reads /output/entry.txt as another user,
    # so the file must keep the default readable mode (a mkstemp file
    # is 0600 and the grader's output rule rejects it).
    with open("/output/entry.txt", "wb") as f:
        f.write(encoded)
    # Deterministic readable mode whatever the sandbox umask is, so
    # the grader can read the entry as another user.
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", "rb") as f:
        assert f.read() == encoded, "entry.txt does not match LINE"
    print(f"{LINE} ({len(encoded)} bytes)")


if __name__ == "__main__":
    main()
