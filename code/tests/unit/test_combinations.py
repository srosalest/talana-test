import pytest

from combinations import get_combinations_from_json, get_starting_player


class TestCombinations:
    def test_given_valid_input_when_get_combinations_from_json_then_return_combinations(
        self, json_valid_input
    ):
        # Given
        json_input_string = json_valid_input

        # When
        get_combinations = get_combinations_from_json(json_input_string)

        # Then
        assert get_combinations == (
            ["D+K", "DSD+P", "S+", "DSD+K", "SD+P"],
            ["SA+K", "SA+", "SA+K", "ASA+P", "SA+P"],
            1,
        )

    def test_given_invalid_input_when_get_combinations_from_json_then_return_combinations(
        self, json_valid_input_empty_movement_and_hit_data
    ):
        # Given
        json_input_string = json_valid_input_empty_movement_and_hit_data

        # When
        get_combinations = get_combinations_from_json(json_input_string)

        # Then
        assert get_combinations is None

    def test_given_players_data_when_get_starting_player_then_return_starting_player(
        self,
    ):
        # Given
        players_data = (
            [["D", "DSD", "S", "DSD", "SD"], ["K", "P", "", "K", "P"]],
            [["SA", "SA", "SA", "ASA", "SA"], ["K", "", "K", "P", "P"]],
        )

        # When
        starting_player = get_starting_player(players_data)

        # Then
        assert starting_player == 1
