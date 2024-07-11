import csv
import heapq
import sys
import timeit


class StateNode:
    def __lt__(self, other):
        return self.heuristic_cost - other.heuristic_cost < 0

    def __init__(self, state, path, current_path_cost, heuristic_cost):
        self.current_path_cost = current_path_cost
        self.heuristic_cost = heuristic_cost
        self.state = state
        self.path = path


def a_star_search(initial, goal):
    frontier = []
    current = StateNode(initial, [initial], 0, 0)
    heapq.heappush(frontier, current)
    reached = {}
    reached[initial] = current
    if initial not in graph or goal not in graph:
        return None
    while frontier:
        current = heapq.heappop(frontier)
        if current.state == goal:
            return current
        for cost, state in graph[current.state]:
            path_cost = current.current_path_cost + cost
            if state not in reached or path_cost < reached[state].current_path_cost:
                new_path = current.path[::] + [state]
                heuristic = path_cost + distances[state, goal]
                neighbor = StateNode(state, new_path, path_cost, heuristic)
                reached[state] = neighbor
                heapq.heappush(frontier, neighbor)
    return None


graph = {}
with open('driving.csv', 'r') as file:
    csvreader = csv.reader(file)
    names = next(csvreader)
    for row in csvreader:
        neighbors = []
        for i in range(1, len(row)):
            row[i] = int(row[i])
            if 0 < row[i]:
                neighbors.append((row[i], names[i]))
        graph[row[0]] = neighbors

distances = {}
with open('straightline.csv', 'r') as file:
    csvreader = csv.reader(file)
    names = next(csvreader)
    for row in csvreader:
        for i in range(1, len(row)):
            row[i] = int(row[i])
            distances[(row[0], names[i])] = row[i]


def greedy_best_first_search(initial, goal):
    current = StateNode(initial, [initial], 0, 0)
    frontier = []
    heapq.heappush(frontier, current)
    reached = {}
    reached[initial] = current
    if initial not in graph or goal not in graph:
        return None
    while frontier:
        current = heapq.heappop(frontier)
        if current.state == goal:
            return current
        for cost, state in graph[current.state]:
            path_cost = current.current_path_cost + cost
            if state not in reached or path_cost < reached[state].current_path_cost:
                new_path = current.path[::] + [state]
                straight_line = distances[state, goal]
                neighbor = StateNode(state, new_path, path_cost, straight_line)
                reached[state] = neighbor
                heapq.heappush(frontier, neighbor)
    return None


distances = {}
with open('straightline.csv', 'r') as file:
    csvreader = csv.reader(file)
    names = next(csvreader)
    for row in csvreader:
        for i in range(1, len(row)):
            row[i] = int(row[i])
            distances[(row[0], names[i])] = row[i]

if len(sys.argv) != 3:
    print('\nERROR: Not enough or too many input arguments.\n')
else:
    print("Dhingra Ronak A20531917 solution:")
    print(f'Initial state: {sys.argv[1]}')
    print(f'Goal state: {sys.argv[2]}\n')

    start = timeit.default_timer()
    goal_node = greedy_best_first_search(sys.argv[1], sys.argv[2])
    stop = timeit.default_timer()
    if goal_node:
        print('Greedy Best First Search:')
        print(f"Solution path: {', '.join(goal_node.path)}")
        print(f'Number of states on path: {len(goal_node.path)}')
        print(f'Path cost: {goal_node.current_path_cost}')
        print(f'Execution time: {stop - start} seconds\n')
    else:
        print('Greedy Best First Search:')
        print('Solution path: FAILURE: NO PATH FOUND')
        print('Number of states on a path: 0')
        print('Path cost: 0')
        print(f'Execution time: {stop - start} seconds\n')

    start = timeit.default_timer()
    goal_node = a_star_search(sys.argv[1], sys.argv[2])
    stop = timeit.default_timer()
    if goal_node:
        print('A* Search:')
        print(f"Solution path: {', '.join(goal_node.path)}")
        print(f'Number of states on path: {len(goal_node.path)}')
        print(f'Path cost: {goal_node.current_path_cost}')
        print(f'Execution time: {stop - start} seconds\n')
    else:
        print('A* Search:')
        print('Solution path: FAILURE: NO PATH FOUND')
        print('Number of states on a path: 0')
        print('Path cost: 0')
        print(f'Execution time: {stop - start} seconds\n')
