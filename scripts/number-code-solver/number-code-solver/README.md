# Number Code Puzzle Solver

A simple Python brute-force solver for **Mastermind-style number code puzzles**. It finds every code that matches a set of clues about digits in the correct or wrong positions.

Requires **Python 3.8+**. No third-party packages needed.

## Quick start

1. Download `solver.py` and `README.md` into the same folder.
2. Open a terminal in that folder.
3. Run:

   ```bash
   python3 solver.py
   ```

   Expected output for the included puzzle:

   ```text
   Found 1 solution(s):
   Answer: 716
   ```

## How it works

1. Python generates every possible 3-digit code, from `012` to `987` when repetition is disabled (including other valid arrangements of those digits).
2. For each candidate, it compares the digits against all five clues.
3. It counts digits in the correct positions and correct digits in the wrong positions.
4. Any candidate that violates even one clue gets eliminated.
5. It prints every code that satisfies all the clues.

## Customize for another puzzle

You only need to change this section in `solver.py`:

```python
clues = [
    ("863", 0, 1),
    ("250", 0, 0),
    ("168", 0, 2),
    ("735", 1, 0),
    ("687", 0, 2),
]
```

Each clue follows this format:

```python
("guess", correct_position, wrong_position)
```

The two counts represent **exactly** how many digits match in each category. Any remaining digits in that guess are absent from the secret code.

For example:

| Clue description | Python format |
| --- | --- |
| 1 digit correct, right place | `("123", 1, 0)` |
| 2 digits correct, wrong place | `("456", 0, 2)` |
| 1 right place, 1 wrong place | `("789", 1, 1)` |
| Nothing correct | `("250", 0, 0)` |

> **CTF tip:** This is a form of a *constraint satisfaction problem (CSP)*. Brute force is excellent for small puzzles, while more complex puzzles can be solved with tools such as Z3 (an SMT solver).

You can also adapt this solver for 4-digit, 5-digit, or 6-digit puzzles by changing `length=3` to the required number of digits **and updating all clue guesses to that length**.

### Allow repeated digits

The default solver only considers codes with distinct digits. To allow repeated digits, set:

```python
answers = solve_puzzle(clues, length=3, allow_repeats=True)
```

### Notes

- Leading zeros are supported (e.g. `012`). Codes are strings, not integers.
- If multiple codes satisfy the clues, all are printed.
- If none do, check whether the clue counts were entered correctly.
- Runtime grows with code length. Without repetition, codes longer than 10 digits are not possible.
