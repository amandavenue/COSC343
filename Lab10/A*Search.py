from eightpuzzle import eightpuzzle
import time
import numpy as np

# actions = puzzle.actions(s=current_state)

# Action A should be 0, 1, 2, 3 (r, u, l, d)
# new_state = puzzle.step(s=current_state, a=A)
# actions_list = list of nums to represent the actions taken to get to the solution
# action_list = list()
# to append -> action_list.append(item)
# to get the nth item use action_list[n]
# to remove the nth item removed_item = action_list.pop(n)

class node:

    def __init__(self, s, parent, cost, action, heuristic):
        self.s = s
        self.parent = parent
        self.cost = cost
        self.action = action
        self.heuristic = heuristic


def heuristic_cost(current, goal):

    current_2d = np.reshape(a=current,newshape=(3, 3))
    goal_2d = np.reshape(a=goal, newshape=(3, 3))

    heuristic_sum = 0

    for x in range (9):
        goal_location = np.array(np.where(goal_2d == x))
        current_location = np.array(np.where(current_2d == x))

        heuristic_sum += np.abs(goal_location-current_location)

    return heuristic_sum


# create a root node
# root = node(s=init_state, parent=None, cost=0, action=None)

# create a child node of the root with the state correspondint to actoion 0 from the initial state
# new_state = puzzle.step(s=init_state, a=0)
# child = node (s=new_state, parent=root, cost=1, action=0)

def main():

    puzzle = eightpuzzle(mode='easy')
    init_state = puzzle.reset()

    # puzzle.show(s=current - state)

    goal_state = puzzle.goal()

    start_time = time.time()

    closed_set = list()
    open_set = list()

    root = node(s=init_state, parent=None, cost=0, action=None,
                         heuristic=heuristic_cost(init_state, puzzle.goal()))
    open_set.append(root)

    while len(open_set) != 0:

        # pop off the state in the open list with the smallest (cost + heuristic)
        min_cost = 9999
        min_index = -1
        for n in range(len(open_set)):
            if open_set[n].cost() + open_set[n].heuristic() < min_cost:
                min_cost = open_set[n].cost + open_set[n].heuristic
                min_index = n

        current_node = open_set.pop(min_index)
        current_state = current_node.s

        # check if the current state is the goal state if it is, then break
        if current_state == goal_state:
            break

        # generate a list of the legal possible actions from the current state
        possible_actions = puzzle.actions(s=current_state)

        # for each of the possible actions of the current state
        for act in possible_actions:
            successor_current_cost = act.cost

            if act in open_set:
                break
            elif act in closed_set:
                break
            else:
                # add the next step in the puzzle to the open list
                open_set.append(node(s=puzzle.step(s=current_state, a=act), parent=current_state,
                                     cost=successor_current_cost, action=act,
                                     heuristic=heuristic_cost(current_state, goal_state)))
            node(s=puzzle.step(s=current_state, a=act), parent=current_state,
                 cost=successor_current_cost, action=act,
                 heuristic=heuristic_cost(current_state, goal_state))
        closed_set.append(node(s=puzzle.step(s=current_state, a=act), parent=current_state, cost=successor_current_cost,
                               action=act, heuristic=heuristic_cost(current_state, goal_state)))

    elapsed_time = (time.time() - start_time)
    print ("Elapsed time: %.1f seconds" % elapsed_time)


if __name__ == "__main__":
    main()