#!/usr/bin/env python3

import re
import sys


CUBE_SIDES = 6


def main():
    print("--- Day 18: Boiling Boulders ---")
    input = tuple(open('input.txt', 'r').readlines())
    print("Solution part 1: " + str(solve_part_1(input)))
    print("Solution part 2: " + str(solve_part_2(input)))


def solve_part_1(input):
    sys.setrecursionlimit(len(input))
    surface_area = 0
    cubes = parse_input(input)
    connected_cubes = []
    while cubes:
        cube = cubes.pop(0)
        cs = iter_connected_cubes(cube, cubes)
        connected_cubes.append(cs)
        for c in cs:
            if c in cubes:
                cubes.remove(c)
    for droplet in connected_cubes:
        surface_area += calculate_surface_area(droplet)
    return surface_area


def solve_part_2(input):
    sys.setrecursionlimit(10000)
    surface_area = 0
    cubes = parse_input(input)
    connected_cubes = []
    big_droplet = set()
    while len(cubes) > 0:
        cube = cubes[0]
        connected = get_connected_cubes(cube, cubes, set()) | {cube}
        connected_cubes.append(connected)
        big_droplet = big_droplet | connected
    for droplet in connected_cubes:
        surface_area += calculate_surface_area(droplet)
    holes = find_holes_in_droplet(big_droplet)
    hole_space = set()
    for x in range(-1, 21):
        for y in range(-1, 21):
            for z in range(-1, 21):
                hole_space.add((x, y, z))
    hole_space = hole_space - big_droplet
    outside = (hole_space - holes)
    to_delete = set()
    holes_visited = set()
    while holes:
        hole = holes.pop()
        if hole not in to_delete and hole not in holes_visited:
            hole_connections = iter_connected_cubes(hole, set(hole_space))
            if len(hole_connections & outside) > 0:
                to_delete = to_delete | hole_connections
                to_delete.add(hole)
            else:
                holes_visited = holes_visited | hole_connections
                holes_visited.add(hole)
                holes = holes - holes_visited
    cubes = parse_input(input)
    for h in holes_visited:
        surface_area -= len(get_directly_connected_cubes(h, cubes))
    return surface_area


def calculate_surface_area(droplet):
    surface_area = 0
    if len(droplet) == 1:
        surface_area += CUBE_SIDES
    else:
        for cube in droplet:
            surface_area += CUBE_SIDES - \
                len(get_directly_connected_cubes(cube, droplet))
    return surface_area


def find_holes_in_droplet(droplet):
    if len(droplet) < 2:
        return set()
    holes = set()
    min_x = min([x[0] for x in droplet])
    min_y = min([x[1] for x in droplet])
    min_z = min([x[2] for x in droplet])
    max_x = max([x[0] for x in droplet])
    max_y = max([x[1] for x in droplet])
    max_z = max([x[2] for x in droplet])
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            ds_in_z = sorted([d for d in droplet if d[0] ==
                             x and d[1] == y], key=lambda d: d[2])
            if len(ds_in_z) > 1:
                for z in range(ds_in_z[0][2] + 1, ds_in_z[-1][2] + 1):
                    hole = (x, y, z)
                    if hole not in droplet and x > min_x and y > min_y and x < max_x and y < max_y and z > min_z and z < max_z:
                        holes.add(hole)
    return holes


def parse_input(input):
    cubes = []
    for line in input:
        c = re.findall('-?\d+\.?\d*', line)
        cubes.append((int(c[0]), int(c[1]), int(c[2])))
    return cubes


def get_connected_cubes(cube, cubes, complete_set):
    if cube in cubes:
        cubes.remove(cube)
    else:
        return set()
    complete_set.add(cube)
    cube_set = {c for c in cubes if connected(cube, c)}
    if len(cube_set) > 0:
        for c in cube_set:
            if c not in complete_set:
                cube_set = cube_set | get_connected_cubes(
                    c, cubes, complete_set)
    return cube_set


def iter_connected_cubes(cube, cubes):
    cube_connections = set()
    cube_connections.add(cube)
    to_visit = [cube]
    visited = set()
    while to_visit:
        start = to_visit.pop(0)
        while start in visited:
            if not to_visit:
                return cube_connections
            start = to_visit.pop(0)
        visited.add(start)
        neighbors = {c for c in cubes if connected(start, c)}
        for c in neighbors:
            cube_connections.add(c)
            if c not in visited:
                to_visit.append(c)
    return cube_connections


def get_connected_holes(cube, cubes, complete_set, outside):
    if cube in outside:
        return set()
    if cube in cubes:
        cubes.remove(cube)
    else:
        return set()
    complete_set.add(cube)
    cube_set = {c for c in cubes if connected(cube, c)}
    if len(cube_set) > 0:
        if len(cube_set & outside) > 0:
            return cube_set
        for c in cube_set:
            if c not in complete_set:
                cube_set = cube_set | get_connected_holes(
                    c, cubes, complete_set, outside)
    return cube_set


def get_directly_connected_cubes(cube, cubes):
    return {c for c in cubes if connected(cube, c)}


def connected(c1, c2):
    diffs = abs(c1[0] - c2[0]), abs(c1[1] - c2[1]), abs(c1[2] - c2[2])
    # A cube only touches if at least two coordinates are the same ...
    if len([d for d in diffs if d == 0]) == 2:
        # ... and the difference for the last coordinate is only 1
        if sum(diffs) == 1:
            return True
    return False


if __name__ == '__main__':
    main()
