from typing import Dict, List, Optional, Union


class Character:
    def __init__(
        self, name: str, energy: int, combinations: Dict[str, List[Union[str, int]]]
    ) -> None:
        self.__name = name
        self.__energy = energy
        self.__combinations = combinations

    def get_name(self) -> str:
        return self.__name

    def get_energy(self) -> int:
        return self.__energy

    def energy_decrease(self, energy: int) -> None:
        self.__energy -= energy

    def get_combination_details(
        self, combination: str
    ) -> Optional[List[Union[str, int]]]:
        for key in self.__combinations.keys():
            if combination.endswith(key):
                return self.__combinations.get(key)

    def get_combinations(self) -> Dict[str, List[Union[str, int]]]:
        return self.__combinations
