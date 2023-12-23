import pytest
import json
from combinations import get_combinations_from_json


class TestCombinations:
    @pytest.fixture
    def json_valid_input(self):
        with open("code/json/input/example_1.json") as f:
            data = json.dumps(json.load(f))
            f.close()
            return data

    @pytest.fixture
    def json_valid_input_empty_movement_and_hit_data(self):
        with open("code/json/input/example_4.json") as f:
            data = json.dumps(json.load(f))
            f.close()
            return data

    def test_given_valid_input_when_get_combinations_from_json_then_return_combinations(self, json_valid_input):
        # Given
        json_input_string = json_valid_input

        # When
        get_combinations = get_combinations_from_json(json_input_string)

        # Then
        assert get_combinations == [
            ["D+K", "DSD+P", "S+", "DSD+K", "SD+P"],
            ["SA+K", "SA+", "SA+K", "ASA+P", "SA+P"],
        ]
    
    def test_given_invalid_input_when_get_combinations_from_json_then_return_combinations(self, json_valid_input_empty_movement_and_hit_data):
        # Given
        json_input_string = json_valid_input_empty_movement_and_hit_data

        # When
        get_combinations = get_combinations_from_json(json_input_string)

        # Then
        assert get_combinations is None