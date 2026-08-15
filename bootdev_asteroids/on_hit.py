import sys

from constants import INVUL_TIME
from logger import log_event


def on_hit(
    health: int, damage: int, player_score: int, high_score: int
) -> tuple[int, float]:
    log_event("player_hit")

    # Apply damage immediately on first impact
    health -= damage

    if health <= 0:
        print(f"You scored {player_score} points!")
        if player_score >= high_score:
            print("Congratulations! A new high score!")
        print("Game over!")
        sys.exit()

    # Return the reduced health and lock the window by returning INVUL_TIME
    return health, INVUL_TIME
