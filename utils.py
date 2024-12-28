import math
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