import dijkstra


def main():
    print("--- Day 12: Hill Climbing Algorithm ---")
    datastream = [l.replace("\n", "")
                  for l in open('input.txt', 'r').readlines()]
    print("Solution part 1: " + str(solve_part_1(datastream)))
    print("Solution part 2: " + str(solve_part_2(datastream)))


def solve_part_1(datastream):
    nodes = []
    graph = dijkstra.Graph()
    populate_graph_and_nodes(nodes, graph, datastream)
    d = dijkstra.DijkstraSPF(graph, find_special_coordinate(datastream, "S"))
    return d.get_distance(find_special_coordinate(datastream, "E"))


def solve_part_2(datastream):
    nodes = []
    graph = dijkstra.Graph()
    populate_graph_and_nodes(nodes, graph, datastream)
    shortest_distance = 1e7
    for node in nodes:
        if get_height(datastream[node[1]][node[0]]) == 1:
            d = dijkstra.DijkstraSPF(graph, node)
            distance = d.get_distance(find_special_coordinate(datastream, "E"))
            if distance < shortest_distance:
                shortest_distance = distance
    return shortest_distance


def populate_graph_and_nodes(nodes, graph, datastream):
    for y, row in enumerate(datastream):
        for x, _ in enumerate(row):
            node = tuple([x, y])
            nodes.append(tuple(node))
            for reachable_node in get_reachable_nodes(node, datastream):
                graph.add_edge(tuple(node), tuple(reachable_node), 1)


def find_special_coordinate(datastream, point):
    for index, line in enumerate(datastream):
        if point in line:
            return tuple([line.index(point), index])
    raise NotImplementedError


def get_reachable_nodes(current_node, datastream):
    nodes = []
    # Left of current coordinate reachable?
    if current_node[0] > 0:
        pos = tuple([current_node[0] - 1, current_node[1]])
        if get_height_difference(current_node, pos, datastream) <= 1:
            nodes.append(pos)
    # Right of current coordinate reachable?
    if current_node[0] < len(datastream[0]) - 1:
        pos = tuple([current_node[0] + 1, current_node[1]])
        if get_height_difference(current_node, pos, datastream) <= 1:
            nodes.append(pos)
    # Top of current coordinate reachable?
    if current_node[1] > 0:
        pos = tuple([current_node[0], current_node[1] - 1])
        if get_height_difference(current_node, pos, datastream) <= 1:
            nodes.append(pos)
    # Down of current coordinate reachable?
    if current_node[1] < len(datastream) - 1:
        pos = tuple([current_node[0], current_node[1] + 1])
        if get_height_difference(current_node, pos, datastream) <= 1:
            nodes.append(pos)
    return nodes


def get_height_difference(current_node, target_node, datastream):
    return get_height(datastream[target_node[1]][target_node[0]]) - get_height(datastream[current_node[1]][current_node[0]])


def get_height(character):
    o = 0
    if character == "S":
        o = ord("a") - 96
    elif character == "E":
        o = ord("z") - 96
    else:
        o = ord(character) - 96
    return o


if __name__ == '__main__':
    main()
