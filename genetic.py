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
    return [(child_solution_a,fitness(child_solution_a)), (child_solution_b,fitness(child_solution_b))]

def naturalSelection (solution_pool):
    elitePool = [x for x in solution_pool if (x[1] > 0)]

    if(verbose):
        printPool("After natural selection:", elitePool)

    return elitePool

def printPool (message, solutionPool):
    print(message)
    for solution in solutionPool:
        print(str(solution[0]) + "  >>  " + str(solution[1]))
    print("\n")

def generatePairs (pool_size, elite_size):
    pairs = []
    while (len(pairs) < pool_size):
        a = random.randint(0, elite_size - 1)
        b = random.randint(0, elite_size - 1)

        if (a != b):
            pairs.append((a, b))

    # for pair in pairs:
    #     print(pair)

    return pairs

def newGeneration (selection_pool, pool_size, generation):
    # Generate pairs for single point crossover function
    pairs = generatePairs(pool_size/2, len(selection_pool))
    new_generation = []

    for pair in pairs:
        new_generation = new_generation + crossover(selection_pool[pair[0]][0],selection_pool[pair[1]][0])

    if (verbose):
        printPool("\nGENERATION " + str(generation) + "\nSolution pool:", new_generation)

    return new_generation

def createInitialPool (pool_size):
    random_solutions = [[random.randint(0,1) for x in range(size)] for y in range(pool_size)]
    initialPool = []

    for solution in random_solutions:
        initialPool.append((solution, fitness(solution)))

    if (verbose):
        printPool("\nGENERATION 0 \nInitial solution pool:", initialPool)

    return initialPool

def main (capacity, object_list, solution, size):
    POOL_SIZE = 10

    # Create Initial Solution Pool
    generation = 0
    initialPool = createInitialPool(POOL_SIZE)

    # Elitism: delete unfit solutions
    elitePool = naturalSelection (initialPool)

    # Create new generation
    generation += 1
    newPool = newGeneration (elitePool, POOL_SIZE, generation)

verbose = True
capacity, object_list, solution, size  = ds.getDataset("KNAPSACK_01/", "1", verbose)

main(capacity, object_list, solution, size)


# TESTING METHODS
#createInitialPool(10)
#fitness([1, 1, 1, 1, 0, 1, 0, 0, 0, 0])
#crossover([1, 1, 0, 1, 0, 0, 0, 0, 0, 0],[1, 0, 1, 0, 0, 1, 0, 0, 1, 1])