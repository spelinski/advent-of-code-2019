"""
Solution to the first challenge of the 2019 Advent of Code
"""

from typing import List
from math import floor

def get_ints_from_file(input_filename: str) -> List[int]:
    """
    Read each line of the file as an integer into a list
    """
    with open(input_filename) as input_file:
        return [int(line) for line in input_file]

def get_fuel_each_element(input_list: List[int]) -> List[int]:
    """
    List of fuel required to launch each element in the list
    """
    return [floor(num/3)-2 for num in input_list if floor(num/3)-2 > 0]

def get_fuel_ignore_fuel_weight(input_list: List[int]) -> int:
    """
    Total fuel needed to launch ignoring the fuel needed to launch the additional fuel
    """
    return sum(get_fuel_each_element(input_list))

def get_fuel_include_fuel_weight(input_list: List[int]) -> int:
    """
    Total fuel needed to launch with additional fuel added to launch the fuel
    """
    fuel_needed = get_fuel_each_element(input_list)
    fuel_needed_sum = 0
    while fuel_needed:
        fuel_needed_sum += sum(fuel_needed)
        fuel_needed = get_fuel_each_element(fuel_needed)
    return fuel_needed_sum

if __name__ == "__main__":
    #Assume list gotten of every number
    MODULE_WEIGHTS = get_ints_from_file("input.txt")

    print("Part 1 answer ignoring weight of fuel")
    print(get_fuel_ignore_fuel_weight(MODULE_WEIGHTS))

    print("Part 2 answer with weight of fuel counted")
    print(get_fuel_include_fuel_weight(MODULE_WEIGHTS))
