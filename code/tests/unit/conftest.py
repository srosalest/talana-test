import json
import pytest

from characters import Character

from constants import (
    ARNALDOR_SHUATSENEGUER,
    HIT_COMBINATION_ARNALDOR_SHUATSENEGUER,
    HIT_COMBINATION_TONYN_STALLONE,
    TONYN_STALLONE,
)

EXAMPLE_1 = "code/json/input/example_1.json"
EXAMPLE_4 = "code/json/input/example_4.json"

@pytest.fixture()
def setup_character_one():
    return Character(
        name=TONYN_STALLONE, energy=6, combinations=HIT_COMBINATION_TONYN_STALLONE
    )

@pytest.fixture()
def setup_character_two():
    return Character(
        name=ARNALDOR_SHUATSENEGUER,
        energy=6,
        combinations=HIT_COMBINATION_ARNALDOR_SHUATSENEGUER,
    )

@pytest.fixture
def json_valid_input():
    with open(EXAMPLE_1) as f:
        data = json.dumps(json.load(f))
        f.close()
        return data

@pytest.fixture
def json_valid_input_empty_movement_and_hit_data():
    with open(EXAMPLE_4) as f:
        data = json.dumps(json.load(f))
        f.close()
        return data