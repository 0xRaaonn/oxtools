"""Brute-force solver for Mastermind-style number code puzzles."""

from collections import Counter
from itertools import permutations, product


def check_clue(code: str, guess: str, correct_place: int, wrong_place: int) -> bool:
    """Return True if code matches exactly the specified clue counts."""
    exact = sum(actual == predicted for actual, predicted in zip(code, guess))
    common = sum((Counter(code) & Counter(guess)).values())
    misplaced = common - exact
    return exact == correct_place and misplaced == wrong_place


def solve_puzzle(clues, length=3, allow_repeats=False):
    """Return every candidate code satisfying all clues (leading zeros allowed)."""
    digits = "0123456789"
    if length < 1 or (length > 10 and not allow_repeats):
        raise ValueError("Invalid code length for selected repetition setting")
    for guess, right, wrong in clues:
        if len(guess) != length or not guess.isdigit():
            raise ValueError(f"Clue {guess!r} must be exactly {length} digits")
        if not (0 <= right <= length and 0 <= wrong <= length - right):
            raise ValueError(f"Invalid clue counts for {guess!r}")

    candidates = (product(digits, repeat=length) if allow_repeats
                  else permutations(digits, length))
    return ["".join(candidate) for candidate in candidates
            if all(check_clue(candidate, guess, right, wrong)
                   for guess, right, wrong in clues)]


# Clue format: ("guess", correct_position, wrong_position)
clues = [
    ("863", 0, 1),  # One digit correct, wrong position
    ("250", 0, 0),  # Nothing correct
    ("168", 0, 2),  # Two digits correct, wrong positions
    ("735", 1, 0),  # One digit correct, right position
    ("687", 0, 2),  # Two digits correct, wrong positions
]

if __name__ == "__main__":
    answers = solve_puzzle(clues, length=3, allow_repeats=False)
    if answers:
        print(f"Found {len(answers)} solution(s):")
        for answer in answers:
            print("Answer:", answer)
    else:
        print("No solution found. Check your clues!")
