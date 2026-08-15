import sys

from constants import INVUL_TIME
from logger import log_event


def on_hit(health: int, damage: int) -> tuple[int, float]:
    log_event("player_hit")

    # Apply damage immediately on first impact
    health -= damage

    if health <= 0:
        print("Game over!")
        sys.exit()

    # Return the reduced health and lock the window by returning INVUL_TIME
    return health, INVUL_TIME
