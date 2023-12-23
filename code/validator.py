import logging
from typing import Dict, Optional, List, Tuple

MOVEMENTS = 0
HITS = 1


def validate_and_sanitize_input(players_input: Optional[Tuple]) -> Optional[Tuple]:
    if players_input:
        player_one, player_two = players_input
        if player_one and player_two:
            player_one_sanitized_input = [
                validate_and_sanitize_movements(player_one[MOVEMENTS]),
                validate_and_sanitize_hits(player_one[HITS]),
            ]
            player_two_sanitized_input = [
                validate_and_sanitize_movements(player_two[MOVEMENTS]),
                validate_and_sanitize_hits(player_two[HITS]),
            ]
            if (None not in player_one_sanitized_input) and (
                None not in player_two_sanitized_input
            ):
                return (player_one_sanitized_input, player_two_sanitized_input)
    logging.error(f"Error: Invalid input, {players_input}")


def validate_and_sanitize_movements(movements: Optional[List]) -> Optional[List]:
    if movements:
        sanitized_movements = []
        for movement in movements:
            if len(movement) > 5:
                movement = ""
            sanitized_movements.append(movement)
        return sanitized_movements


def validate_and_sanitize_hits(hits: Optional[List]) -> Optional[List]:
    if hits:
        sanitized_hits = []
        for hit in hits:
            if len(hit) > 1:
                hit = ""
            sanitized_hits.append(hit)
        return sanitized_hits
