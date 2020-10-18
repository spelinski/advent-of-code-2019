from dataclasses import dataclass
from typing import List, Dict, Tuple

@dataclass
class PathCrossing:
    first_wire: bool = False
    second_wire: bool = False
    first_steps: int = 0
    second_steps: int = 0

class CircuitBoard:
    def __init__(self, first_wire_path: List[str], second_wire_path: List[str]):
        self.circuit = {} # type: Dict[Tuple[int,int], PathCrossing]
        self.first_path_taken = first_wire_path.copy()
        self.second_path_taken = second_wire_path.copy()
        self._add_wire("first")
        self._add_wire("second")

    def _handle_adding_wire_point(self, current_idx: Tuple[int,int], wire_place: str, step: int):
        wire_name = wire_place + "_wire"
        step_name = wire_place + "_steps"
        add_cross = self.circuit.get(current_idx, PathCrossing())
        if getattr(add_cross, wire_name) == False:
            setattr(add_cross, wire_name, True)
            setattr(add_cross, step_name, step)
            self.circuit[current_idx] = add_cross

    def _add_wire(self, wire_place: str):
        path_name = wire_place + "_path_taken"
        current_idx = (0,0)
        step = 1
        for movement in getattr(self, path_name):
            direction = movement[0]
            step_goal = int(movement[1::])
            while step_goal > 0:
                if direction == "R":
                    current_idx = (current_idx[0]+1, current_idx[1])
                elif direction == "L":
                    current_idx = (current_idx[0]-1, current_idx[1])
                elif direction == "U":
                    current_idx = (current_idx[0], current_idx[1]+1) 
                elif direction == "D":
                    current_idx = (current_idx[0], current_idx[1]-1) 
                self._handle_adding_wire_point(current_idx, wire_place, step)
                step += 1
                step_goal -= 1

    def find_min_manhatten_distance(self) -> int:
        min_distance = pow(2,32) - 1
        for point,cross in self.circuit.items():
            if cross.first_wire == True and cross.second_wire == True:
                if(abs(point[0])+abs(point[1]) < min_distance):
                    min_distance = abs(point[0]) + abs(point[1])
        return min_distance

    def find_min_steps(self) -> int:
        min_steps = pow(2,32) - 1
        for cross in self.circuit.values():
            if cross.first_wire == True and cross.second_wire == True:
                if cross.first_steps + cross.second_steps < min_steps:
                    min_steps = cross.first_steps + cross.second_steps
        return min_steps

