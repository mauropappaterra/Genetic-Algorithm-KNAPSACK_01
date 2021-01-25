# Genetic Algorithm - KNAPSACK_01
# genetic.py
# Created by Mauro José Pappaterra on 25 January 2021.
import create_dataset as ds
import random

def fitness (solution):
    total_weight = sum([object_list[solution.index(x)].weight for x in solution if (x == 1)])
    # print(total_weight)
    if (total_weight > capacity):
        return 0

    total_profit = sum([object_list[solution.index(x)].profit for x in solution if (x == 1)])
    # print(total_profit)
    return total_profit

def crossover (solution_a, solution_b):
    random_partition = random.randint(1, size - 1)
    # print(random_partition)
    child_solution_a = solution_a[:random_partition] + solution_b[random_partition:]
    # print(child_solution_a)
    child_solution_b = solution_b[:random_partition] + solution_a[random_partition:]
    # print(child_solution_b)
    return [[child_solution_a,fitness(child_solution_a)], [child_solution_b,fitness(child_solution_b)]]

def createInitialPool (pool_size):
    random_solutions = [[random.randint(0,1) for x in range(size)] for y in range(pool_size)]
    initialPool = []

    for solution in random_solutions:
        initialPool.append([solution, fitness(solution)])

    if (verbose):
        print ("GENERATION 0 \nInitial solution pool:")
        for solution in initialPool:
            print(str(solution))

    return initialPool

def main (capacity, object_list, solution, size, verbose):
    GENERATION = 0
    POOL_SIZE = 10

    # Create Initial Solution Pool
    initialPool = createInitialPool(POOL_SIZE)


verbose = True
capacity, object_list, solution, size  = ds.getDataset("KNAPSACK_01/", "1", verbose)

main(capacity, object_list, solution, size, verbose)


# TESTING METHODS
#createInitialPool(10)
#fitness([1, 1, 1, 1, 0, 1, 0, 0, 0, 0])
#crossover([1, 1, 0, 1, 0, 0, 0, 0, 0, 0],[1, 0, 1, 0, 0, 1, 0, 0, 1, 1])