# Genetic Algorithm
# create_dataset.py
# Created by Mauro José Pappaterra on 25 January 2021.

class newObject ():
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit

def getDataset (path, dataset, verbose):

    object_list = []

    with open (path + "p0" + dataset + "_c.txt", 'r') as file:
        capacity = int(file.readlines()[0])

    with open(path + "p0" + dataset + "_s.txt", 'r') as file:
        solution = [int(x) for x in file.readlines()if True]

    with open (path + "p0" + dataset + "_w.txt", 'r') as file:
        weights = [int(x) for x in file.readlines()if True]

    with open(path + "p0" + dataset + "_p.txt", 'r') as file:
        profits = [int(x) for x in file.readlines()if True]

    for i, o in enumerate(solution):
        object_list.append(newObject(weights[i], profits[i]))

    if (verbose):
        print ("\n=== Dataset " + dataset + " ===\n\nobject   weight   profit   solution")
        for i, object in enumerate(object_list):
            print("  " + str(i) + "        " + str(object.weight) + "       " + str(object.profit) + "         " + str(solution[i]))
        print("\nCapacity: " + str(capacity) + "\nOptimal Solution: " + str(solution))

    return (capacity, object_list, solution)

# path = "KNAPSACK_01/"
# dataset1 = getDataset(path, "1", True)
# dataset2 = getDataset(path, "2", True)
# dataset3 = getDataset(path, "3", True)
# dataset4 = getDataset(path, "4", True)
# dataset5 = getDataset(path, "5", True)
# dataset6 = getDataset(path, "6", True)
# dataset7 = getDataset(path, "7", True)

# print (dataset1[0])
# print (str(dataset1[1][9].profit))
# print (str(dataset1[2]))