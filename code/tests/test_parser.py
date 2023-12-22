import pytest
import json

from parser import json_parser, parse_movements, parse_hits

class TestParser:
    @pytest.fixture
    def jsonInputOne(self):
        with open('code/json/input/example_1.json') as f:
            data = json.dumps(json.load(f))
            f.close()
            return data


    def test_json_parser(self, jsonInputOne):
        # Given 
        jsonInputString = jsonInputOne

        # When
        parsed_data = json_parser(jsonInputString)

        # Then
        assert json_parser(jsonInputOne) == (
            [
                ['D', 'DSD', 'S', 'DSD', 'SD'], 
                ['K', 'P', '', 'K', 'P']
            ], 
            [
                ['SA', 'SA', 'SA', 'ASA', 'SA'],
                 ['K', '', 'K', 'P', 'P'],
            ],
        )
   

    def test_parse_movements(self, jsonInputOne):
        # Given
        json_input = json.loads(jsonInputOne)
        player_one = json_input.get("player1")
        player_two = json_input.get("player2")

        # When
        movements_player_one = parse_movements(player_one)
        movements_player_two = parse_movements(player_two)

        # Then
        assert  movements_player_one == ['D', 'DSD', 'S', 'DSD', 'SD']
        assert  movements_player_two == ['SA', 'SA', 'SA', 'ASA', 'SA']

    def test_parse_hits(self, jsonInputOne):
        # Given
        json_input = json.loads(jsonInputOne)
        player_one = json_input.get("player1")
        player_two = json_input.get("player2")

        # When
        hits_player_one = parse_hits(player_one)
        hits_player_two = parse_hits(player_two)

        # Then
        assert  hits_player_one == ['K', 'P', '', 'K', 'P']
        assert  hits_player_two == ['K', '', 'K', 'P', 'P']
