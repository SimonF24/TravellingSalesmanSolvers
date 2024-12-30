from collections import deque
import random
from typing import List, Tuple

from utils import get_route_distance

def tabu_solver(
    cities: List[Tuple[float, float]], num_iterations: int = 1000, num_neighbors: int = 3,
    tabu_max_size: int = 10) -> Tuple[List[Tuple[float, float]], float]:
    """
    Solves the travelling salesman problem using a tabu search algorithm.
    
    params:
        cities - The cities to visit represented as a list of (x, y) coordinates
        num_iterations - The number of iterations to run the tabu search for
        num_neighbors - The number of neighbors to consider in each iteration
        tabu_max_size - The maximum size of the tabu list
        
    returns:
        best_route, best_route_distance - The best route found and its distance
    """
    best_route = cities.copy()
    random.shuffle(best_route)
    best_route_distance = get_route_distance(best_route)
    current_route = best_route.copy()
    tabu_list = deque((best_route))
    for _ in range(num_iterations):
        best_neighbor_distance = float('inf')
        # Swapping adjacent cities in the route to generate neighboring routes
        for _ in range(num_neighbors):
            i1 = random.randint(0, len(cities) - 1)
            i2 = (i1 + 1) % len(cities)
            neighbor_route = current_route.copy()
            neighbor_route[i1], neighbor_route[i2] = neighbor_route[i2], neighbor_route[i1]
            if neighbor_route in tabu_list:
                continue
            neighbor_route_distance = get_route_distance(neighbor_route)
            if neighbor_route_distance < best_neighbor_distance:
                current_route = neighbor_route
                current_route_distance = neighbor_route_distance
                
        # Accepting the new route if it is better
        if current_route_distance < best_route_distance:
            best_route = current_route.copy()
            best_route_distance = current_route_distance
            
        # Adding the current route to the tabu list
        tabu_list.append(current_route)
        while len(tabu_list) > tabu_max_size:
            tabu_list.popleft()
    return best_route, best_route_distance