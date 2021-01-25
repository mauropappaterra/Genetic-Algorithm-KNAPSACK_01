# Genetic Algorithm
# genetic.py
# Created by Mauro José Pappaterra on 25 January 2021.

import create_dataset as ds

capacity, object_list, solution = ds.getDataset("KNAPSACK_01/", "1", False)

print (capacity)
print(object_list[0].profit)
print(solution)