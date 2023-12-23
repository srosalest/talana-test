import pytest
import json

from validator import (
    validate_and_sanitize_input,
    validate_and_sanitize_movements,
    validate_and_sanitize_hits,
)

PLAYER_ONE = 0
PLAYER_TWO = 1
MOVEMENTS = 0
HITS = 1


class TestValidator:
    @pytest.fixture
    def valid_parsed_input(self):
        return (
            [["D", "DSD", "S", "DSD", "SD"], ["K", "P", "", "K", "P"]],
            [
                ["SA", "SA", "SA", "ASA", "SA"],
                ["K", "", "K", "P", "P"],
            ],
        )

    @pytest.fixture
    def nil_and_invalid_movements_input(self):
        return (
            [None, ["K", "P", "", "K", "P"]],
            [
                ["SASASA", "SA", "SA", "ASA", "SA"],
                None,
            ],
        )

    @pytest.fixture
    def nil_and_invalid_hits_input(self):
        return (
            [
                ["D", "DSD", "S", "DSD", "SD"],
                None,
            ],
            [
                None,
                ["KK", "", "K", "P", "P"],
            ],
        )

    def test_given_valid_input_when_validate_and_sanitize_input_then_return_sanitized_input(
        self, valid_parsed_input
    ):
        # Given
        players_input = valid_parsed_input

        # When
        sanitized_input = validate_and_sanitize_input(players_input)

        # Then
        assert sanitized_input == (
            [["D", "DSD", "S", "DSD", "SD"], ["K", "P", "", "K", "P"]],
            [["SA", "SA", "SA", "ASA", "SA"], ["K", "", "K", "P", "P"]],
        )

    def test_given_nil_and_invalid_movements_input_when_validate_and_sanitize_input_then_return_sanitized_input(
        self, nil_and_invalid_movements_input
    ):
        # Given
        players_input = nil_and_invalid_movements_input

        # When
        sanitized_input = validate_and_sanitize_input(players_input)

        # Then
        assert sanitized_input is None

    def test_given_nil_and_invalid_movements_when_validate_and_sanitize_movements_then_return_sanitized_movements(
        self, nil_and_invalid_movements_input
    ):
        # Given
        nill_movements = nil_and_invalid_movements_input[PLAYER_ONE][MOVEMENTS]
        invalid_movements = nil_and_invalid_movements_input[PLAYER_TWO][MOVEMENTS]

        # When
        player_one_movements = validate_and_sanitize_movements(nill_movements)
        player_two_movements = validate_and_sanitize_movements(invalid_movements)

        # Then
        assert player_one_movements is None
        assert player_two_movements == ["", "SA", "SA", "ASA", "SA"]

    def test_given_nil_and_invalid_hits_when_validate_and_sanitize_hits_then_return_sanitized_hits(
        self, nil_and_invalid_hits_input
    ):
        # Given
        nill_hits = nil_and_invalid_hits_input[PLAYER_ONE][HITS]
        invalid_hits = nil_and_invalid_hits_input[PLAYER_TWO][HITS]

        # When
        player_one_hits = validate_and_sanitize_hits(nill_hits)
        player_two_hits = validate_and_sanitize_hits(invalid_hits)

        # Then
        assert player_one_hits is None
        assert player_two_hits == ["", "", "K", "P", "P"]
