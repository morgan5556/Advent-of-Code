"""
Advent of Code 2024
Day 1 - https://adventofcode.com/2024/day/1

Solution by Morgan Lyons
"""

# Imports the read file function
import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from read_file import read_file

# Solution
def main():
    # Gets the input for the selected day and year
    input = read_file(2024, 1)

    p1 = part_one(input)
    p2 = part_two(input)

    print(f"Part One: {p1}")
    print(f"Part Two: {p2}")


def part_one(input):
    list_1, list_2 = split_numbers_into_lists(input)
    list_1, list_2 = sort_lists(list_1, list_2)
    total_difference = compare_lists(list_1, list_2)

    return total_difference

def part_two(input):
    list_1, list_2 = split_numbers_into_lists(input)
    similarity_list = iterate_through_list(list_1, list_2)
    
    return sum(similarity_list)

def split_numbers_into_lists(input):
    list_1 = []
    list_2 = []

    for line in input.splitlines():
        numbers = line.split()

        num_1 = int(numbers[0])
        num_2 = int(numbers[1])

        list_1.append(num_1)
        list_2.append(num_2)

    return list_1, list_2

def sort_lists(list_1, list_2):
    list_1 = sorted(list_1)
    list_2 = sorted(list_2)

    return list_1, list_2

def compare_lists(list_1, list_2):
    difference_list = []
    for x, y in zip(list_1, list_2):
        difference_list.append(abs((x) - (y)))
    
    return sum(difference_list)

def iterate_through_list(list_1, list_2):
    similarity_list = []
    for x in list_1:
        similarity = list_2.count(x) * x
        similarity_list.append(similarity)

    return similarity_list

if __name__ == "__main__":
    main()