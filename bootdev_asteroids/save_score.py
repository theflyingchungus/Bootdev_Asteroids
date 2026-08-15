import os

HIGH_SCORE_FILE = "highscore.txt"


def load_high_score(filepath=HIGH_SCORE_FILE) -> int:
    if not os.path.exists(filepath):
        return 0
    try:
        with open(filepath, "r") as f:
            return int(f.read().strip())
    except (ValueError, IOError):
        return 0


def save_high_score(score: int, filepath=HIGH_SCORE_FILE):
    try:
        with open(filepath, "w") as f:
            f.write(str(score))
    except IOError as e:
        print(f"Failed to save high score: {e}")
