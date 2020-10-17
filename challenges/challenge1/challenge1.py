from typing import List
from math import floor

def get_ints_from_file(input_filename: str) -> List[int]:
    with open(input_filename) as input_file:
        return [int(line) for line in input_file]

def get_fuel_needed_each_module(input_list: List[int]):
    return [floor(num/3)-2 for num in input_list if floor(num/3)-2 > 0]


if __name__ == "__main__":
    #Assume list gotten of every number
    module_weights = get_ints_from_file("input.txt")
    fuel_needed_each_module = get_fuel_needed_each_module(module_weights)

    print("Part 1 answer ignoring weight of fuel")
    fuel_needed_total = sum(fuel_needed_each_module)
    print(fuel_needed_total)

    fuel_needed_additional = get_fuel_needed_each_module(fuel_needed_each_module)
    while(sum(fuel_needed_additional) > 0):
        fuel_needed_total += sum(fuel_needed_additional)
        fuel_needed_additional = get_fuel_needed_each_module(fuel_needed_additional)
    print("Part 2 answer with weight of fuel counted")
    print(fuel_needed_total)            
