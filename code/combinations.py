from parser import json_parser
from validator import validate_and_sanitize_input
from typing import Optional, List


def get_combinations_from_json(
    json_input_string: Optional[str],
) -> Optional[List[List[str]]]:
    if json_input_string:
        if parsed_and_sanitized_data := validate_and_sanitize_input(
            json_parser(json_input_string)
        ):
            player_one, player_two = parsed_and_sanitized_data
            if player_one and player_two:
                player_one_combination = __merge_combinations(player_one)
                player_two_combination = __merge_combinations(player_two)
                return [player_one_combination, player_two_combination]


def __merge_combinations(player_data: List[List[str]]) -> List[str]:
    movements, hits = player_data
    movements_length = len(movements)
    hits_length = len(hits)
    player_combination = []
    for index in range(movements_length):
        player_combination.append(f"{movements[index]}+{hits[index]}")
    return player_combination
