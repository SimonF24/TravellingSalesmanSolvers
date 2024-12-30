import math
import random
from typing import List, Tuple


def get_intercity_distance(city1: Tuple[float, float], city2: Tuple[float, float]) -> float:
    """
    Gets the distance between two cities represented as (x, y) coordinates.
    """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)


def get_route_distance(cities: List[Tuple[float, float]]) -> float:
    """
    Gets the total distance of a route that visits all cities ((x, y) coordinates) in the order
    given and returns to the first city.
    """
    distance = 0
    for i in range(len(cities)):
        city1 = cities[i]
        city2 = cities[i-1]
        distance += get_intercity_distance(city1, city2)
    return distance


def quickselect(routes: List[List[Tuple[float, float]]], k: int) -> List[List[Tuple[float, float]]]:
    """
    Sorts the top k routes in the given list of routes in place using quickselect.
    """
    if k > len(routes):
        raise ValueError('k must be less than or equal to the number of routes')
    left, right = 0, len(routes) - 1
    while left <= right:
        pivot_index = quickselect_partition(routes, left, right)
        if pivot_index == k:
            return routes[:k]
        elif pivot_index > k:
            right = pivot_index - 1
        else:
            left = pivot_index + 1


def quickselect_partition(routes: List[List[Tuple[float, float]]], left: int, right: int) -> int:
    """
    Partitions the given list of routes in place using Hoare's partitioning scheme.
    """
    pivot = left
    i = left - 1
    j = right + 1
    while True:
        i += 1
        while get_route_distance(routes[i]) < get_route_distance(routes[pivot]):
            i += 1
        j -= 1
        while get_route_distance(routes[j]) > get_route_distance(routes[pivot]):
            j -= 1
        if i >= j:
            return j
        routes[i], routes[j] = routes[j], routes[i]