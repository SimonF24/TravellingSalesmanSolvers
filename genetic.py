import random
from typing import List, Tuple

from utils import get_route_distance

def genetic_solver(
    cities: List[Tuple[float, float]], population_size: int = 3, num_iterations: int = 100,
    num_mutations: int = 3, num_children: int = 3) -> Tuple[List[Tuple[float, float]], float]:
    """
    Solves the travelling salesman problem using a genetic algorithm.
    
    params:
        cities - The cities to visit represented as a list of (x, y) coordinates
        population_size - The size of the population to use in the genetic algorithm
        
    returns:
        best_route, best_route_distance - The best route found and its distance
    """
    population = [random.sample(cities, len(cities)) for _ in range(population_size)]
    for _ in range(num_iterations):
        population_additions = []
        # Mutate through swapping adjacent cities in the route
        for _ in range(num_mutations):
            mutant = random.choice(population).copy()
            i1 = random.randint(0, len(cities) - 1)
            i2 = (i1 + 1) % len(cities)
            mutant[i1], mutant[i2] = mutant[i2], mutant[i1]
            population_additions.append(mutant)
        
        # Partially mapped crossover
        for _ in range(num_children):
            i1, i2 = random.sample(range(len(cities) + 1), 2)
            if i1 > i2:
                i1, i2 = i2, i1
            parent1, parent2 = random.sample(population, 2)
            child = []
            for k in range(len(cities)):
                if i1 <= k < i2:
                    child.append(parent1[k])
                else:
                    child.append(None)
            for k in range(i1, i2):
                if parent2[k] not in child[i1:i2]:
                    p1_index = parent1.index(child[k])
                    if not child[p1_index]:
                        child[p1_index] = parent2[k]
                    else:
                        blocker_p2_index = parent2.index(child[p1_index])
                        child[blocker_p2_index] = parent2[k]
            child_set = set(child)
            p2_index = 0
            child_index = 0
            while child_index < len(cities):
                if not child[child_index]:
                    while parent2[p2_index] in child_set:
                        p2_index += 1
                    child[child_index] = parent2[p2_index]
                    child_set.add(parent2[p2_index])
                child_index += 1
            population_additions.append(child)
            
        population += population_additions
        population.sort(key=lambda route: get_route_distance(route))
        # This could be improved by partitioning e.g. quickselect, I'm omitting for simplicity,
        # since the population size is small and since it isn't a focus of this project
        population = population[:population_size]
        
    return population[0], get_route_distance(population[0])