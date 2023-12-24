from typing import Dict, List, Optional, Union

from constants import MOVEMENTS


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
            if key == combination:
                combination_values = self.__combinations.get(key).copy()
                combination_values.append(
                    f"{self.__name} combina un {combination_values[1]}"
                )
                return combination_values
            else:
                if combination.endswith(key):
                    if key in combination:
                        combination = combination.replace(key, "")
                    relator = ""
                    if combination.endswith("+"):
                        combination = combination[:-1]
                    for item in combination:
                        if movement := MOVEMENTS.get(item):
                            relator += movement
                    combination_values = self.__combinations.get(key).copy()
                    combination_values.append(
                        f"{self.__name} {relator}y combina un {combination_values[1]}"
                    )
                    return combination_values

        if combination.endswith("+"):
            combination = combination[:-1]
        relator = ""
        for item in combination:
            if movement := MOVEMENTS.get(item):
                relator += movement
        combination_values = self.__combinations.get(key).copy()
        combination_values.append(
            f"{self.__name} {relator}y combina un {combination_values[1]}"
        )
        return combination_values

    def get_combinations(self) -> Dict[str, List[Union[str, int]]]:
        return self.__combinations
