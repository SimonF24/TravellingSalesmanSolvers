from typing import Literal

from simulated_annealing import simulated_annealing_solver

solver_to_use: Literal["simulated_annealing"] = "simulated_annealing"

if __name__ == "__main__":
    # The cities are represented as (x, y) coordinates that the salesman needs to visit
    # The salesman can start and end at any city, but must end at the same city
    cities = [
        (0, 0),   # City 0
        (10, 10), # City 1
        (20, 20), # City 2
        (5, 15),  # City 3
        (15, 5),  # City 4
        (25, -5)  # City 5
    ]
    if solver_to_use == "simulated_annealing":
        found_route, found_route_distance = simulated_annealing_solver(cities)
    else:
        raise ValueError(f"Unknown solver: {solver_to_use}")
    # Appending the first city to the end to close the route
    # Note that many routes can be equivalent and these techniques are not guaranteed to find the optimal route,
    # so the route may differ betweens run
    found_route.append(found_route[0])
    print(f"Found route: {found_route}")
    print(f"Found route distance: {found_route_distance}")