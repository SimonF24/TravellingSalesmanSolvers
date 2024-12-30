from itertools import combinations
import random
from typing import List, Tuple

from utils import get_intercity_distance

def held_karp_solver(cities: List[Tuple[float, float]]) -> Tuple[List[Tuple[float, float]], float]:
    """
    Solves the travelling salesman problem using the Held-Karp (Bellman-Held-Karp) algorithm.
    
    params:
        cities - The cities to visit represented as a list of (x, y) coordinates
        
    returns:
        best_route, best_route_distance - The best route found and its distance
    """
    # This uses a binary representation of the set of visited cities that is 0 if a city isn't
    # present and 1 if it is. I'll show an equivalent set representation in the comments.
    
    # The starting city doesn't matter so we choose the first one, route here stores indices of cities
    min_distances = {}
    # The keys to min_distances are tuples containing (set of visited cities, last_city)
    # The values are tuples containing (distance, previous_city) 
    for i in range(1, len(cities)):
        min_distances[(1 << i, i)] = (get_intercity_distance(cities[0], cities[i]), 0)
        # Equivalent set representation
        # min_distances[({i}, i)] = (get_intercity_distance(cities[0], cities[i]), 0)
    
    # Build up the minimum distances dictionary for each subset of cities
    for size in range(2, len(cities)):
        for combo in combinations(range(1, len(cities)), size):
            
            visited_cities = 0
            for bit in combo:
                visited_cities |= 1 << bit
            
            # Equivalent set representation
            # visited_cities = set(combo)
            
            # Cycle through ending at each city in the combination and find the minimum distance
            for end in combo:
                min_distance = float('inf')
                best_prev = None
                without_end = visited_cities ^ (1 << end) 
                
                # Equivalent set representation
                # without_end = subset - {end}
                
                # Try each possible previous city to find the best one
                for prev in combo:
                    if prev == end:
                        continue
                    distance = min_distances[(without_end, prev)][0] + get_intercity_distance(cities[prev], cities[end])
                    if distance < min_distance:
                        min_distance = distance
                        best_prev = prev
                        
                min_distances[(visited_cities, end)] = (min_distance, best_prev)

    # Returning to the starting city
    visited_cities = (1 << len(cities)) - 2 # All cities except the starting city
    # Equivalent set representation
    # visited_cities = set(range(1, len(cities)))
    min_distance = float('inf')
    best_prev = None
    for prev in range(1, len(cities)):
        distance = min_distances[(visited_cities, prev)][0] + get_intercity_distance(cities[prev], cities[0])
        # Equivalent set representation
        # distance = min_distances[(set(range(1, len(cities))), prev)][0] + get_intercity_distance(cities[prev], cities[0])
        if distance < min_distance:
            min_distance = distance
            best_prev = prev
    best_route_distance = min_distance 
    
    # Reconstruction of the best route
    route = [0]
    prev = best_prev
    remaining = visited_cities
    for _ in range(len(cities) - 1):
        route.append(prev)
        next_prev = min_distances[(remaining, prev)][1]
        remaining ^= 1 << prev
        # Equivalent set representation
        # remaining.remove(prev)
        prev = next_prev
        
    
    # Converting back to (x, y) coordinates
    best_route = []
    for city in route:
        best_route.append(cities[city])
    
    return best_route, best_route_distance