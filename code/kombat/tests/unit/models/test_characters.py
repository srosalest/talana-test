import pytest

from models.characters import Character
from constants import (
    ARNALDOR_SHUATSENEGUER,
    ARNALDOR_SHUATSENEGUER_HIT_1,
    HIT_COMBINATION_ARNALDOR_SHUATSENEGUER,
    HIT_COMBINATION_TONYN_STALLONE,
    TONYN_STALLONE,
    TONYN_STALLONE_HIT_1,
)


class TestCharacters:
    def test_given_characters_when_get_name_then_return_name(
        self, setup_character_one, setup_character_two
    ):
        # Given
        first_character = setup_character_one
        second_character = setup_character_two

        # When
        first_character_name = first_character.get_name()
        second_character_name = second_character.get_name()

        # Then
        assert first_character_name == TONYN_STALLONE
        assert second_character_name == ARNALDOR_SHUATSENEGUER

    def test_given_characters_when_get_energy_then_return_energy(
        self, setup_character_one, setup_character_two
    ):
        # Given
        first_character = setup_character_one
        second_character = setup_character_two

        # When
        first_character_energy = first_character.get_energy()
        second_character_energy = second_character.get_energy()

        # Then
        assert first_character_energy == 6
        assert second_character_energy == 6

    def test_given_characters_when_energy_decrease_then_update_energy(
        self, setup_character_one, setup_character_two
    ):
        # Given
        first_character = setup_character_one
        second_character = setup_character_two

        # When
        first_character.energy_decrease(1)
        second_character.energy_decrease(1)

        # Then
        assert first_character.get_energy() == 5
        assert second_character.get_energy() == 5

    def test_given_characters_when_get_combinations_then_return_combinations(
        self, setup_character_one, setup_character_two
    ):
        # Given
        first_character = setup_character_one
        second_character = setup_character_two

        # When
        first_character_combinations = first_character.get_combinations()
        second_character_combinations = second_character.get_combinations()

        # Then
        assert first_character_combinations == HIT_COMBINATION_TONYN_STALLONE
        assert second_character_combinations == HIT_COMBINATION_ARNALDOR_SHUATSENEGUER

    def test_given_characters_when_get_combination_details_return_combination_details(
        self, setup_character_one, setup_character_two
    ):
        # Given
        first_character = setup_character_one
        second_character = setup_character_two

        first_character_exact_combination = TONYN_STALLONE_HIT_1
        second_character_exact_combination = ARNALDOR_SHUATSENEGUER_HIT_1
        first_character_noisy_combination = "D" + TONYN_STALLONE_HIT_1
        second_character_noisy_combination = "D" + ARNALDOR_SHUATSENEGUER_HIT_1

        # When
        first_character_combination_details = first_character.get_combination_details(
            first_character_exact_combination
        )
        second_character_combination_details = second_character.get_combination_details(
            second_character_exact_combination
        )

        first_character_noisy_combination_details = (
            first_character.get_combination_details(first_character_noisy_combination)
        )
        second_character_noisy_combination_details = (
            second_character.get_combination_details(second_character_noisy_combination)
        )

        # Then
        assert (
            first_character_combination_details[2]
            == "Tonyn Stallone combina un Taladoken"
        )
        assert (
            second_character_combination_details[2]
            == "Arnaldor Shuatseneguer combina un Taladoken"
        )
        assert (
            first_character_noisy_combination_details[2]
            == "Tonyn Stallone se mueve a la derecha y combina un Taladoken"
        )
        assert (
            second_character_noisy_combination_details[2]
            == "Arnaldor Shuatseneguer se mueve a la derecha y combina un Taladoken"
        )
