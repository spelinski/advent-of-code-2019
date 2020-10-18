from typing import List
from CircuitBoard import CircuitBoard

def get_both_paths_from_file(input_filename: str) -> List[List[str]]:
    list_of_lists = []
    with open(input_filename) as input_file:
        for line in input_file:
            list_of_lists.append([movement for movement in line.split(",")])
    return list_of_lists

if __name__ == "__main__":
    ALL_PATHS = get_both_paths_from_file("input.txt")
    SHIPS_BOARD = CircuitBoard(ALL_PATHS[0], ALL_PATHS[1])
    print("Solution to first part of problem")
    print(SHIPS_BOARD.find_min_manhatten_distance())
    print("solution to second part of problem")
    print(SHIPS_BOARD.find_min_steps())
