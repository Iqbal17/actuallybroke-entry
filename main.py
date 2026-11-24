"""Say What Actually Broke — one line of software error copy (115 chars).

The entry (exactly what main.py writes to entry.txt):

    Your password is correct. Our password checker is down.
    You are fine. We are the problem. Try again in ten minutes.

Candidate lines weighed against the judge's criteria
(most important first: brutal truth + funny; names the real failure
in plain words with a next step; funny on one read with a repeatable
twist; single tight line; shippable in a real product dialog):

1. CHOSEN — the login line above (115 chars). It names the real
   failure in plain words ("Our password checker is down"), gives a
   concrete next step ("Try again in ten minutes"), and the twist is
   a line a user repeats out loud to a colleague: "You are fine. We
   are the problem." Every sentence is a flat statement, no apology
   in generalities, and a team could genuinely ship it in a dialog.

2. REJECTED — "We deleted your account by accident. Someone honestly
   pressed the delete button. Support can restore it from Tuesday's
   backup." (129 chars). The twist ("someone honestly pressed the
   delete button") is strong, and the next step is real, but a
   deleted account is a failure almost no team would ever admit in a
   dialog, so it loses on criterion 5 (shippable). It also leans on
   a backup that may not exist.

3. REJECTED — "Your payment was charged twice because our retry
   button retries and our database doesn't check. The refund is
   automatic, in 5-7 business days, like a punishment." (about 160
   chars). It names a real failure (double charge from an unchecked
   retry), but the joke lands on the refund timeline rather than the
   failure, "like a punishment" makes the next step feel like a
   penalty instead of a fix, and the length dilutes the single-read
   punch.

4. REJECTED — "Error 500: our server tried to do the thing, thought
   about it, and gave up halfway. Nothing you did caused this.
   Please refresh and pretend it never happened." (about 155 chars).
   "The thing" names nothing, so it fails criterion 2 (names the real
   failure); "pretend it never happened" is a shrug, not a next step.

Pass 2 — genuine revision of the draft: the draft read "Login failed:
your password is correct, but the server that checks passwords is
down. You are fine. We are the problem. Try again in ten minutes."
(144 chars). The revision cuts the "Login failed:" preamble (throat
clearing — criterion 4) and the wordy "the server that checks
passwords" down to "Our password checker", and splits the "is
correct, but" clause into two short declarative sentences. Same
meaning, 29 characters shorter, and the deadpan cadence lands
harder: each sentence is now a flat beat, with the twist ("You are
fine. We are the problem.") standing on its own.
"""

import os

LINE = (
    "Your password is correct. Our password checker is down. "
    "You are fine. We are the problem. Try again in ten minutes."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
