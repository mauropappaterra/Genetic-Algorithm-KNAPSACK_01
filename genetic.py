# Genetic Algorithm - KNAPSACK_01
# genetic.py
# Created by Mauro José Pappaterra on 25 January 2021.
import create_dataset as ds
import random
import math

def createInitialPool (object_list, size, capacity, pool_size, verbose):
    random_solutions = [[random.randint(0,1) for x in range(size)] for y in range(pool_size)]
    initialPool = []

    for genome in random_solutions:
        initialPool.append((genome, fitness(genome, object_list, capacity)))

    if (verbose):
        printPool("\nGENERATION 0 \nInitial solution pool:", initialPool)

    return initialPool

def fitness (genome, object_list, capacity):

    total_weight = sum([object_list[i].weight for i,x in enumerate(genome) if (x == 1)])

    if (total_weight > capacity):
        return 0

    total_profit = sum([object_list[i].profit for i,x in enumerate(genome) if (x == 1)])
    return total_profit

def naturalSelection (genome_pool, verbose):
    elitePool = [x for x in genome_pool if (x[1] > 0)]

    if (len(elitePool) == 0): # when no natural selection is possible
        return genome_pool
    elif (len(elitePool) == 1): # when only 1 genome makes it to natural selection
        random_genome = [x for x in genome_pool if (x not in elitePool)][0]
        elitePool.append(random_genome)

    elitePool.sort(key=lambda x:x[1], reverse=True)

    if(verbose):
        printPool("\nAfter natural selection:", elitePool)

    return elitePool

def printPool (message, genomePool):
    print(message)
    for genome in genomePool:
        print(str(genome[0]) + "  >>  " + str(genome[1]))


def mutation (genome, size, mutation_probability):
    nonce = round(random.uniform(0, 1),2)

    if (nonce <= mutation_probability):
        randomIndex = random.randint(0, size - 1)
        genome[randomIndex] = abs(genome[randomIndex] - 1)

    return genome

def newGeneration (object_list, size, capacity, pool_size, elite_size, elite_pool, mutation_probability, generation, verbose):
    # Keep best n solutions from previous generation elite pool
    new_generation = elite_pool[:elite_size]

    if (verbose):
        printPool("\nGENERATION " + str(generation) + "\nKeeping best " + str(elite_size) + " genome solutions from generation " + str(generation - 1), new_generation)

    # Generate pairs for single point crossover function
    pairs = generatePairs((pool_size - elite_size) / 2, len(elite_pool))

    for pair in pairs:
        new_generation = new_generation + crossover(elite_pool[pair[0]][0], elite_pool[pair[1]][0], object_list, size, capacity, mutation_probability)

    if (verbose):
        printPool("\nSolution pool:", new_generation)

    return new_generation

def generatePairs (pool_size, elite_pool_size):
    pairs = []
    while (len(pairs) < pool_size):
        a = random.randint(0, elite_pool_size - 1)
        b = random.randint(0, elite_pool_size - 1)

        if (a != b):
            pairs.append((a, b))

    return pairs

def crossover (renome_a, genome_b, object_list, size, capacity, mutation_probability):
    random_partition = random.randint(1, size - 1)
    # print(random_partition)
    child_genome_a = renome_a[:random_partition] + genome_b[random_partition:]
    child_genome_a = mutation(child_genome_a, size, mutation_probability)
    # print(child_genome_a)
    child_genome_b = genome_b[:random_partition] + renome_a[random_partition:]
    child_genome_b = mutation(child_genome_b, size, mutation_probability)
    # print(child_genome_b)

    return [(child_genome_a,fitness(child_genome_a, object_list, capacity)), (child_genome_b,fitness(child_genome_b, object_list, capacity))]

def checkSolution (genome_pool, solution):
    find_solutions = [x[0] for x in genome_pool]
    return solution in find_solutions

def geneticAlgorithm (object_list, size, capacity, solution, pool_size, elite_size, mutation_probability, verbose):
    generation = 0

    # Create Initial Solution Pool 
    pool = createInitialPool(object_list, size, capacity, pool_size, verbose)

    while (not checkSolution(pool, solution)):
        generation += 1
        # Elitism: delete unfit solutions and keep best solutions from previous generation
        elitePool = naturalSelection (pool, verbose)
        # Create new generation
        pool = newGeneration (object_list, size, capacity, pool_size, elite_size, elitePool, mutation_probability, generation, verbose)

    print ("\nFound optimal solution after " + str(generation) + " generations")
    printPool("\nSolution Pool:", pool)
    print("\nOptimal Solution: " + str(solution) + "  >>  " + str(fitness(solution, object_list, capacity)) )

# Global variables
POOL_SIZE = 10
ELITE_SIZE = 2 # no. of solutions to keep from each generation after natural selection
MUTATION_PROBABILITY = 0.50
VERBOSE = False

# Database variabless
OBJECT_LIST, SIZE, CAPACITY, SOLUTION = ds.getDataset("KNAPSACK_01/", "7", VERBOSE)

geneticAlgorithm(OBJECT_LIST, SIZE, CAPACITY, SOLUTION, POOL_SIZE, ELITE_SIZE, MUTATION_PROBABILITY, VERBOSE)