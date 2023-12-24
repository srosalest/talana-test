import itertools
import json
import sys
from typing import List, Optional, Type

from characters import Character
from combinations import get_combinations_from_json
from constants import (
    ARNALDOR_SHUATSENEGUER,
    HIT_COMBINATION_ARNALDOR_SHUATSENEGUER,
    HIT_COMBINATION_TONYN_STALLONE,
    TONYN_STALLONE,
)

PARAMETER_INDEX = 2
MIN_ENERGY = 0


def setup_brawl(json_input_string: Optional[str]) -> None:
    player_one = Character(
        name=TONYN_STALLONE, energy=6, combinations=HIT_COMBINATION_TONYN_STALLONE
    )
    player_two = Character(
        name=ARNALDOR_SHUATSENEGUER,
        energy=6,
        combinations=HIT_COMBINATION_ARNALDOR_SHUATSENEGUER,
    )
    if combinations := get_combinations_from_json(json_input_string):
        player_one_combination, player_two_combination, starting_player = combinations
        brawl(
            player_one,
            player_two,
            player_one_combination,
            player_two_combination,
            starting_player,
        )


def brawl(
    player_one: Type[Character],
    player_two: Type[Character],
    player_one_combination: [List[str]],
    player_two_combination: [List[str]],
    starting_player: int,
) -> None:
    for player_one_action, player_two_action in itertools.zip_longest(
        player_one_combination, player_two_combination
    ):
        if starting_player == 1:
            if player_turn(player_one, player_two, player_one_action):
                return
            if player_turn(player_two, player_one, player_two_action):
                return
        else:
            if player_turn(player_two, player_one, player_two_action):
                return
            if player_turn(player_one, player_two, player_one_action):
                return


def player_turn(
    current_player: Type[Character], target_player: Type[Character], action: str
) -> Optional[bool]:
    if action:
        damage, _, relator = current_player.get_combination_details(action)
        print(relator)
        target_player.energy_decrease(damage)
        if target_player.get_energy() <= MIN_ENERGY:
            print(
                f"{current_player.get_name()} ha ganado y le queda {current_player.get_energy()} energia"
            )
            return True


if __name__ == "__main__":
    arg = sys.argv[PARAMETER_INDEX]
    if arg.endswith(".json"):
        with open(arg) as f:
            arg = json.dumps(json.load(f))
            f.close()
    setup_brawl(json_input_string=arg)
