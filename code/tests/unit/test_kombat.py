import pytest

from constants import TONYN_STALLONE_HIT_1
from kombat import player_turn

class TestKombat:
    def test_given_last_action_when_player_turn_then_return_true(self, setup_character_one, setup_character_two):
        # Given
        player_one = setup_character_one
        player_two = setup_character_two
        player_two.energy_decrease(3)
        action = TONYN_STALLONE_HIT_1

        # When
        expected_output = player_turn(player_one, player_two, action)

        # Then
        assert expected_output is True
        assert player_two.get_energy() == 0

    def test_given_action_when_player_turn_then_return(self, setup_character_one, setup_character_two):
        # Given
        player_one = setup_character_one
        player_two = setup_character_two
        action = TONYN_STALLONE_HIT_1

        # When
        expected_output = player_turn(player_one, player_two, action)

        # Then
        assert expected_output is None
        assert player_two.get_energy() == 3
