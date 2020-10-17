"""
Solution to the second challenge in the 2019 Advent of Code
"""
from typing import Dict
from itertools import product

def get_line_from_file(input_filename: str) -> Dict[int, int]:
    """
    Read comma seperated integers all on the same line
    """
    with open(input_filename) as input_file:
        list_of_nums = [int(num) for num in input_file.readline().split(",")]
        return {idx: list_of_nums[idx] for idx in range(0, len(list_of_nums))}

def run_program(program_memory: Dict[int, int], noun: int, verb: int) -> Dict[int, int]:
    """
    Runs the program while overiding memory locations 1 and 2 with noun and verb
    """
    program_memory[1] = noun
    program_memory[2] = verb
    i = 0
    while i < len(program_memory):
        if program_memory[i] == 1:
            first_number = program_memory[program_memory[i+1]]
            second_number = program_memory[program_memory[i+2]]
            output_idx = program_memory[i+3]
            program_memory[output_idx] = first_number + second_number
        elif program_memory[i] == 2:
            first_number = program_memory[program_memory[i+1]]
            second_number = program_memory[program_memory[i+2]]
            output_idx = program_memory[i+3]
            program_memory[output_idx] = first_number * second_number
        elif program_memory[i] == 99:
            break
        else:
            print("Ran into an unknown opcode")
            break
        i += 4
    return program_memory

if __name__ == "__main__":
    INITIAL_MEMORY = get_line_from_file("input.txt")
    print("solution to the first problem")
    print(run_program(INITIAL_MEMORY.copy(), 12, 2)[0])

    for combo in product(range(0, 100), repeat=2):
        if run_program(INITIAL_MEMORY.copy(), combo[0], combo[1])[0] == 19690720:
            print("solution to the second problem")
            print((100*combo[0])+ combo[1])
            break
