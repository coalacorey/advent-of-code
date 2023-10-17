#!/usr/bin/env python3
import re


def main():
    print("--- Day 15: Beacon Exclusion Zone ---")
    input = open('input.txt', 'r').readlines()
    print("Solution part 1: " + str(solve_part_1(input)))
    print("Solution part 2: " + str(solve_part_2(input)))


def solve_part_1(input):
    sensor_dict, beacons = parse_input(input)
    blocked = set()
    row = 2000000
    for sensor in find_sensors_affecting_row(sensor_dict, row):
        dist_to_row = abs(row - sensor[1])
        x_to_check = sensor_dict[sensor] - dist_to_row
        for x in range(sensor[0] - x_to_check, sensor[0] + x_to_check + 1):
            if ((x, row)) not in blocked:
                if manhatten_distance(sensor, (x, row)) <= sensor_dict[sensor]:
                    blocked.add((x, row))
    beacons_in_row = set([(b[0], b[1]) for b in beacons if b[1] == row])
    return len(blocked) - len(beacons_in_row)


def solve_part_2(input):
    lower_bound = 0
    upper_bound = 4000000
    sensor_dict, _beacons = parse_input(input)
    res = 0
    for row in range(lower_bound, upper_bound):
        ranges = []
        for sensor in find_sensors_affecting_row(sensor_dict, row):
            dist_to_row = abs(row - sensor[1])
            x_to_check = sensor_dict[sensor] - dist_to_row
            r = (max(lower_bound, sensor[0] - x_to_check),
                 min(upper_bound, sensor[0] + x_to_check))
            ranges.append(r)
        ranges.sort(key=lambda x: x[0])
        if (lower_bound, upper_bound) not in ranges:
            full_range = ranges[0]
            for partial_range in ranges[1:]:
                if full_range[1] in range(partial_range[0], partial_range[1]):
                    full_range = (full_range[0], partial_range[1])
            if full_range != (lower_bound, upper_bound):
                res = (full_range[1] + 1, row)
                return res[0] * upper_bound + res[1]
    return 0


def find_sensors_affecting_row(sensor_dict, row):
    sensors = []
    for sensor in sensor_dict:
        if sensor[1] < row:
            if sensor[1] + sensor_dict[sensor] >= row:
                sensors.append(sensor)
        if sensor[1] > row:
            if sensor[1] - sensor_dict[sensor] <= row:
                sensors.append(sensor)
        if sensor[1] == row:
            sensors.append(sensor)
    return sensors


def parse_input(input):
    sensor_dict = dict()
    sensors = []
    beacons = []
    for line in input:
        temp = re.findall('-?\d+\.?\d*', line)
        res = list(map(int, temp))
        sensors.append([res[0], res[1]])
        beacons.append([res[2], res[3]])
    for i, sensor in enumerate(sensors):
        sensor_dict[(sensor[0], sensor[1])] = manhatten_distance(
            sensor, beacons[i])
    return sensor_dict, beacons


def manhatten_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == '__main__':
    main()
