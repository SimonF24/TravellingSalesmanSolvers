import random
from typing import List, Tuple

from utils import get_intercity_distance, get_route_distance


def brute_force_solver(cities: List[Tuple[float, float]]) -> Tuple[List[Tuple[float, float]], float]:
    """
    Solves the travelling salesman problem using brute force.
    
    params:
        cities - The cities to visit represented as a list of (x, y) coordinates
    
    returns:
        best_route, best_route_distance - The best route found and its distance
    """
    best_distance = [get_route_distance(cities)]
    best_route = cities.copy()
    random_city = random.choice(best_route) # The starting city doesn't matter so we choose a random one
    backtrack(cities, [random_city], set([random_city]), 0, best_route, best_distance)
    return best_route, best_distance[0]


def backtrack(
    cities: List[Tuple[float, float]], current_route: List[Tuple[float, float]],
    current_visited_cities: set[Tuple[float, float]], current_distance: float,
    best_route: List[Tuple[float, float]], best_distance: List[float]) -> None:
    """
    Recursive function to backtrack through all possible routes.
    
    params:
        cities - The cities to visit represented as a list of (x, y) coordinates
        current_route - The current partial route being explored
        current_visited_cities - The cities that have already been visited in the current partial route
        current_distance - The current distance of the partial route
        best_route - The best route found so far
        best_distance - A list where the first element is the best distance found so far
        
    returns:
        None
    """
    if len(current_route) == len(cities):
        current_distance += get_intercity_distance(current_route[-1], current_route[0])
        if current_distance < best_distance[0]:
            best_distance[0] = current_distance
            for i in range(len(current_route)):
                best_route[i] = current_route[i]
        return
    elif current_distance >= best_distance[0]:
        return
    for city in cities:
        if city in current_visited_cities:
            continue
        new_distance = current_distance
        if len(current_route) > 0:
            new_distance += get_intercity_distance(current_route[-1], city)
        current_visited_cities.add(city)
        backtrack(cities, current_route + [city], current_visited_cities, new_distance, best_route, best_distance)
        current_visited_cities.remove(city)