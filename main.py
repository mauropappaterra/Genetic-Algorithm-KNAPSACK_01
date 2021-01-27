# Genetic Algorithm - KNAPSACK_01
# main.py
# Created by Mauro José Pappaterra on 25 January 2021.
import create_dataset as ds
import genetic_algorithm as ga

# Global variables
POOL_SIZE = 100
ELITE_SIZE = 10 # no. of solutions to keep from each generation after natural selection
MUTATION_PROBABILITY = 0.50
VERBOSE = False

for dataset in list(range(1,9)):
    # Database variables
    OBJECT_LIST, SIZE, CAPACITY, SOLUTION = ds.getDataset("KNAPSACK_01/", str(dataset), True)
    ga.geneticAlgorithm(OBJECT_LIST, SIZE, CAPACITY, SOLUTION, POOL_SIZE, ELITE_SIZE, MUTATION_PROBABILITY, VERBOSE)