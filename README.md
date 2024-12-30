# Travelling Salesman Solvers
A collection of simple implementations of algorithms solving the travelling salesman problem. The travelling salesman
problem is to find the shortest route through a list of cities, visiting each city once and returning to the original
city. We consider the problem in 2D for simplicity, the extension to 3D is trivial. All algorithms
are implemented in pure Python with only standard library packages.

To run simply run main.py with solver_to_use set to the solution technique you'd like to use.

Algorithms Implemented:
- Exact
  - Brute Force
  - Held-Karp (Bellman-Held-Karp) Algorithm
- Approximate
  - Simulated Annealing
  - Genetic Algorithm
  - Tabu Search