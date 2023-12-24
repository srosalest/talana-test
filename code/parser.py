import json
from typing import Dict, Optional, List, Tuple


def json_parser(json_input_string: Optional[str]) -> Optional[Tuple]:
    if json_input_string:
        try:
            json_input = json.loads(json_input_string)
        except:
            return
        player_one = json_input.get("player1")
        player_two = json_input.get("player2")
        if player_one and player_two:
            player_one_input = [parse_movements(player_one), parse_hits(player_one)]
            player_two_input = [parse_movements(player_two), parse_hits(player_two)]
            return (player_one_input, player_two_input)


def parse_movements(player: Dict) -> Optional[Dict]:
    movements = player.get("movimientos")
    if movements:
        return movements


def parse_hits(player: Dict) -> Optional[Dict]:
    hits = player.get("golpes")
    if hits:
        return hits
