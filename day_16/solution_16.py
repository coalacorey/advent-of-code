#!/usr/bin/env python3
import dijkstra
import re
import functools
from itertools import permutations


MOVE_TIME = 1
VALVE_OPEN_TIME = 1
TIME_LIMIT_1 = 26


@functools.lru_cache(maxsize=None)
def main():
    print("--- Day 16: Proboscidea Volcanium ---")
    input = tuple(open('input.txt', 'r').readlines())
    parse_input(input)
    print("Solution part 1: " + str(solve_part_1(input)))
    print("Solution part 2: " + str(solve_part_2(input)))


@functools.lru_cache(maxsize=None)
def solve_part_1(input):
    valve_connections, valve_flow_rate, valve_visited = parse_input(input)
    graph = dijkstra.Graph()
    graph = populate_graph(valve_connections, graph)
    current_path = [v for v in valve_flow_rate.keys()
                    if valve_flow_rate[v] > 0]

    high_score = 0
    for i in range(2, len(current_path) + 1):
        lp = permutations(current_path, i)
        permutation = next(lp, None)
        while permutation != None:
            score = simulate(permutation, graph,
                             valve_visited, valve_flow_rate, TIME_LIMIT_1)
            if score > high_score:
                high_score = score
            permutation = next(lp, None)
        print(str(i) + ": " + str(high_score))

    return high_score


# @functools.lru_cache(maxsize=None)
def simulate(path, graph, valve_visited, valve_flow_rate, time_limit):
    minute = 1
    total_pressure = 0
    pressure_per_minute = 0
    current_valve = "AA"

    r = 1
    while minute <= time_limit:
        total_pressure += pressure_per_minute
        # print("== Minute " + str(abs(time)) + " ==\n")
        # print("Valves: " + str([v for v in valve_visited.keys() if valve_visited[v] ==
        #               True]) + " are open, releasing " + str(pressure_per_minute) + " pressure.\n")
        if r < len(path):
            for target_valve in path:
                r += 1
                distance = get_distance(graph, current_valve, target_valve)
                for i in range(1, distance + VALVE_OPEN_TIME + 1):
                    if i == distance + 1:
                        # valve_visited[target_valve] = True
                        pressure_per_minute += valve_flow_rate[target_valve]
                    minute += 1
                    # print("== Minute " + str(abs(time)) + " ==\n")
                    # print("Valves: " + str([v for v in valve_visited.keys() if valve_visited[v] ==
                    #     True]) + " are open, releasing " + str(pressure_per_minute) + " pressure.\n")
                    total_pressure += pressure_per_minute
                    if minute == time_limit:
                        return total_pressure
                current_valve = target_valve
        minute += 1

    return total_pressure


def populate_graph(v_c, graph: dijkstra.Graph):
    for valve in v_c.keys():
        graph.add_edge(valve, valve, 0)
        for connection in v_c[valve]:
            graph.add_edge(valve, connection, MOVE_TIME)
    return graph


@functools.lru_cache(maxsize=None)
def get_distance(graph, start_valve, target_valve):
    d_search = dijkstra.DijkstraSPF(graph, start_valve)
    distance = d_search.get_distance(target_valve)
    return distance


def parse_input(input):
    valve_connections = dict()
    valve_flow_rate = dict()
    valve_visited = dict()
    for line in input:
        valve = str(line[6:8])
        valve_visited[valve] = False
        digits = re.findall('-?\d+\.?\d*', line)
        fr = int(digits[0])
        valve_flow_rate[valve] = fr
        targets = re.findall(r"\b[A-Z]{2}\b", line[line.find(";") + 2:])
        valve_connections[valve] = targets
    return valve_connections, valve_flow_rate, valve_visited


def solve_part_2(input):
    valve_connections, valve_flow_rate, valve_visited = parse_input(input)
    graph = dijkstra.Graph()
    graph = populate_graph(valve_connections, graph)
    current_path = [v for v in valve_flow_rate.keys()
                    if valve_flow_rate[v] > 0]

    high_score_1 = 0
    solution_path = []
    for i in range(2, len(current_path)):
        lp = permutations(current_path, i)
        permutation = next(lp, None)
        while permutation != None:
            score = simulate(permutation, graph,
                             valve_visited, valve_flow_rate, TIME_LIMIT_1)
            if score > high_score_1:
                high_score_1 = score
                solution_path = permutation
            permutation = next(lp, None)
    print("Me: " + str(high_score_1))

    for item in solution_path:
        if item in current_path:
            current_path.remove(item)

    high_score_2 = 0
    for i in range(2, len(current_path) + 1):
        lp = permutations(current_path, i)
        permutation = next(lp, None)
        while permutation != None:
            score = simulate(permutation, graph,
                             valve_visited, valve_flow_rate, TIME_LIMIT_1)
            if score > high_score_2:
                high_score_2 = score
            permutation = next(lp, None)
    print("Elefant: " + str(high_score_2))

    return high_score_1 +  high_score_2

if __name__ == '__main__':
    main()
