import itertools
from typing import Optional, List

from combinations import get_combinations_from_json
from characters import Character
from constants import (
    HIT_COMBINATION_TONYN_STALLONE,
    HIT_COMBINATION_ARNALDOR_SHUATSENEGUER,
    TONYN_STALLONE,
    ARNALDOR_SHUATSENEGUER,
)


def setup_brawl(json_input_string: Optional[str]) -> None:
    player_one = Character(
        name=TONYN_STALLONE, energy=6, combinations=HIT_COMBINATION_TONYN_STALLONE
    )
    player_two = Character(
        name=ARNALDOR_SHUATSENEGUER,
        energy=6,
        combinations=HIT_COMBINATION_ARNALDOR_SHUATSENEGUER,
    )
    player_one_combination, player_two_combination, starting_player = get_combinations_from_json(json_input_string)
    

def brawl(player_one, player_two, player_one_combination, player_two_combination, starting_player) -> None:
    for (player_one_action, player_two_action) in itertools.zip_longest(player_one_combination, player_two_combination):
        if starting_player == 1:
            if player_turn(player_one, player_two, player_one_action): return
            if player_turn(player_two, player_one, player_two_action): return
        else:
            if player_turn(player_two, player_one, player_two_action): return
            if player_turn(player_one, player_two, player_one_action): return

    
def player_turn(current_player, target_player, action) -> Optional[bool]: 
    if action:
        damage, _, relator = current_player.get_combination_details(action)
        print(relator)
        target_player.energy_decrease(damage)
        if target_player.get_energy() <= 0:
            print(f"{current_player.get_name()} ha ganado")
            return True
