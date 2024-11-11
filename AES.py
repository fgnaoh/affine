from enum import Enum
from collections import namedtuple

Location = Enum('Location',['A','B'])
State = namedtuple('State',['man','cabbage','goat','wolf'])

def is_valid(state):
    goat_eats_cabbage = (state.goat == state.cabbage and state.man != state.goat)
    wofl_eats_goat = (state.wolf == state.goat and state.man != state.wolf)
    return not (goat_eats_cabbage or wofl_eats_goat)
def depth_first_search(start, is_goal, get_neighbors):
    parent = dict()
    to_visit =[start]
    discovered = set([start])
    while to_visit:
        vertex = to_visit.pop()
        if is_goal(vertex):
            path = []
            while vertex is not None:
                path.insert(0, vertex)
                vertex = parent.get(vertex)
            return path
        
        for neighbor in get_neighbors(vertex):
            if neighbor not in discovered and is_valid(neighbor):
                discovered.add(neighbor)
                parent[neighbor] = vertex
                to_visit.append(neighbor)

start_state = State(man = Location.A,cabbage = Location.A, goat = Location.A, wolf = Location.A)
goal_state = State(man = Location.B,cabbage = Location.B, goat = Location.B, wolf = Location.B)

def get_neighbors(state):
    neighbors = []
    for obj in ['man','cabbage','goat','wolf']:
        if getattr(state, obj) == state.man:
            new_location = Location.A if state.man == Location.B else Location.B
            new_state = State(** {k: new_location if k == obj or k =='man' else v for k, v in state._asdict().items()})
            neighbors.append(new_state)
        return neighbors

path = depth_first_search(start=start_state, is_goal=goal_state.__eq__,get_neighbors=get_neighbors)
for state in path:
    print(state)
            
