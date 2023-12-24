import json
from parser import json_parser, parse_hits, parse_movements

import pytest


class TestParser:
    def test_given_valid_input_when_json_parser_then_return_parsed_data(
        self, json_valid_input
    ):
        # Given
        json_input_string = json_valid_input

        # When
        parsed_data = json_parser(json_input_string)

        # Then
        assert parsed_data == (
            [["D", "DSD", "S", "DSD", "SD"], ["K", "P", "", "K", "P"]],
            [
                ["SA", "SA", "SA", "ASA", "SA"],
                ["K", "", "K", "P", "P"],
            ],
        )

    def test_given_valid_input_when_json_parser_then_return_parsed_data(
        self, json_valid_input_empty_movement_and_hit_data
    ):
        # Given
        json_input_string = json_valid_input_empty_movement_and_hit_data

        # When
        parsed_data = json_parser(json_input_string)

        # Then
        assert parsed_data == (
            [None, ["P", ""]],
            [
                ["", "ASA", "DA", "AAA", "", "SA"],
                None,
            ],
        )

    def test_given_player_movement_data_when_parse_movements_then_return_player_movement(
        self, json_valid_input
    ):
        # Given
        json_input = json.loads(json_valid_input)
        player_one = json_input.get("player1")
        player_two = json_input.get("player2")

        # When
        movements_player_one = parse_movements(player_one)
        movements_player_two = parse_movements(player_two)

        # Then
        assert movements_player_one == ["D", "DSD", "S", "DSD", "SD"]
        assert movements_player_two == ["SA", "SA", "SA", "ASA", "SA"]

    def test_given_player_empty_movement_data_when_parse_movements_then_return_empty_list(
        self, json_valid_input_empty_movement_and_hit_data
    ):
        # Given
        json_input = json.loads(json_valid_input_empty_movement_and_hit_data)
        player_one = json_input.get("player1")
        player_two = json_input.get("player2")

        # When
        movements_player_one = parse_movements(player_one)
        movements_player_two = parse_movements(player_two)

        # Then
        assert movements_player_one == None
        assert movements_player_two == ["", "ASA", "DA", "AAA", "", "SA"]

    def test_given_player_valid_date_when_parse_hits_return_player_hits(
        self, json_valid_input
    ):
        # Given
        json_input = json.loads(json_valid_input)
        player_one = json_input.get("player1")
        player_two = json_input.get("player2")

        # When
        hits_player_one = parse_hits(player_one)
        hits_player_two = parse_hits(player_two)

        # Then
        assert hits_player_one == ["K", "P", "", "K", "P"]
        assert hits_player_two == ["K", "", "K", "P", "P"]

    def test_given_player_empty_hit_data_when_parse_hits_then_return_empty_list(
        self, json_valid_input_empty_movement_and_hit_data
    ):
        # Given
        json_input = json.loads(json_valid_input_empty_movement_and_hit_data)
        player_one = json_input.get("player1")
        player_two = json_input.get("player2")

        # When
        movements_player_one = parse_hits(player_one)
        movements_player_two = parse_hits(player_two)

        # Then
        assert movements_player_one == ["P", ""]
        assert movements_player_two == None
