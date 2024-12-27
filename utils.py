import math
from typing import List, Tuple

def get_route_distance(cities: List[Tuple[int, int]], route: List[int]):
    """
    Gets the total distance of a route that visits all cities in the order given
    and returns to the first city.
    """
    distance = 0
    for i in range(len(cities)):
        city1 = cities[i]
        city2 = cities[i-1]
        distance += math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
    return distance