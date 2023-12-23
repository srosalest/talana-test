from parser import json_parser
from validator import validate_and_sanitize_input
from typing import Optional, List, Union, Tuple


def get_combinations_from_json(
    json_input_string: Optional[str],
) -> Optional[List[List[Union[str, int]]]]:
    if json_input_string:
        if parsed_and_sanitized_data := validate_and_sanitize_input(
            json_parser(json_input_string)
        ):
            starting_player = get_starting_player(parsed_and_sanitized_data)
            player_one, player_two = parsed_and_sanitized_data
            if player_one and player_two:
                player_one_combination = __merge_combinations(player_one)
                player_two_combination = __merge_combinations(player_two)
                return [player_one_combination, player_two_combination, starting_player]


def get_starting_player(players_data: Tuple[List[List[str]]]) -> int:
    player_one, player_two = players_data
    player_one_combinations_qty = __count_combinations(player_one)
    player_two_combinations_qty = __count_combinations(player_two)

    if player_one_combinations_qty[0] != player_two_combinations_qty[0]:
        values = [0, player_one_combinations_qty[0], player_two_combinations_qty[0]]
        return values.index(max(values))

    elif player_one_combinations_qty[1] != player_two_combinations_qty[1]:
        values = [0, player_one_combinations_qty[1], player_two_combinations_qty[1]]
        return values.index(max(values))

    elif player_one_combinations_qty[2] != player_two_combinations_qty[2]:
        values = [0, player_one_combinations_qty[2], player_two_combinations_qty[2]]
        return values.index(max(values))

    return 1


def __count_combinations(player_data: List[List[str]]) -> List[int]:
    movements, hits = player_data
    clean_movements = list(filter(None, movements))
    clean_hits = list(filter(None, hits))
    return [len(clean_movements + clean_hits), len(clean_movements), len(clean_hits)]


def __merge_combinations(player_data: List[List[str]]) -> List[str]:
    movements, hits = player_data
    player_combination = []
    for index in range(len(movements)):
        player_combination.append(f"{movements[index]}+{hits[index]}")
    return player_combination
