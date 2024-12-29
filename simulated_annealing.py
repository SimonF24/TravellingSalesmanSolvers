import math
import random
from typing import List, Tuple

from utils import get_route_distance


def simulated_annealing_solver(
    cities: List[Tuple[float, float]], initial_temp: float=100, num_iterations: int=1000,
    cooling_rate: float=0.995, restart_after: int=50, restart_distance: float = 10,
    swap_neighboring: bool = True)-> Tuple[List[Tuple[float, float]], float]:
    """
    Solves the travelling salesman problem using simulated annealing with restarts.
    The parameters can be tuned to improve performance.
    
    params:
        cities - The cities to visit represented as a list of (x, y) coordinates
        initial_temp - The initial temperature for the simulated annealing
        num_iterations - The number of iterations to run the simulated annealing for
        cooling_rate - The rate at which to cool the temperature
        restart_after - The number of iterations without improvement to restart the search
        restart_distance - The distance threshold to trigger a restart
        swap_neighboring - Whether to swap neighboring cities in the route (random cities are swapped if False)
        
    returns:
        best_route, best_route_distance - The best route found and its distance
    """
    best_route = cities.copy()
    random.shuffle(best_route)
    best_route_distance = get_route_distance(best_route)
    current_route = best_route
    current_route_distance = best_route_distance
    since_best = 0
    temperature = initial_temp
    for _ in range(num_iterations):
        # Swapping two cities in the route to generate a neighboring route
        if swap_neighboring:
            i1 = random.randint(0, len(cities) - 1)
            i2 = (i1 + 1) % len(cities)
        else:
            i1, i2 = random.sample(range(len(cities) - 1), 2)
            if i1 == i2:
                continue
        new_route = current_route.copy()
        new_route[i1], new_route[i2] = new_route[i2], new_route[i1]
        new_route_distance = get_route_distance(new_route)
        
        # Accepting the new route if it is better or with a decreasing probability if it is worse
        if (new_route_distance < current_route_distance
            or random.random() < math.exp(current_route_distance - new_route_distance / temperature)):
            # Note that this exponential relies on being used knowing that new_route_distance >= current_route_distance
            # so the numerator is negative and therefore the exponential is between 0 and 1 so it can be interpreted
            # as a probability distribution
            current_route = new_route
            current_route_distance = new_route_distance
        elif (since_best >= restart_after
              or current_route_distance > best_route_distance + restart_distance):
            # Restarting the search if no improvement has been made for a while or the route is too far from the best
            current_route = best_route.copy()
            current_route_distance = best_route_distance
            since_best = 0
            
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