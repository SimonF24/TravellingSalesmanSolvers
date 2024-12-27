import math
import random
from typing import List

from utils import get_route_distance

def simulated_annealing_solver(cities: List[int], initial_temp: float=100, max_iterations: int=1000, cooling_rate: float=0.995, restart_after: int=50):
    """
    Solves the travelling salesman problem using simulated annealing.
    """
    best_route = cities.copy()
    random.shuffle(best_route)
    best_route_distance = get_route_distance(cities, best_route)
    current_route = best_route
    current_route_distance = best_route_distance
    since_best = 0
    temperature = initial_temp
    for i in range(max_iterations):
        # Swapping two cities in the route to generate a neighboring route
        i1, i2 = random.sample(range(len(cities) - 1), 2)
        if i1 == i2:
            continue
        new_route = current_route.copy()
        new_route[i1], new_route[i2] = new_route[i2], new_route[i1]
        new_route_distance = get_route_distance(cities, new_route)
        
        # Accepting the new route if it is better or with a decreasing probability if it is worse
        if (new_route_distance < current_route_distance
            or since_best > restart_after
            or random.random() < math.exp(current_route_distance - new_route_distance / temperature)):
            # Note that this exponential relies on being used knowing that new_route_distance >= current_route_distance
            # so the numerator is negative and therefore the exponential is between 0 and 1 so it can be interpreted
            # as a probability distribution
            current_route = new_route
            current_route_distance = new_route_distance
            
        # Updating the best route if the current route is better
        if current_route_distance < best_route_distance:
            best_route = current_route.copy()
            best_route_distance = current_route_distance
            since_best = 0
        else:
            since_best += 1
        
        # Lowering the temperature
        temperature *= cooling_rate
        
        return best_route, best_route_distance