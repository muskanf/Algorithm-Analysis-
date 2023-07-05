import random
import time
import matplotlib.pyplot as plt

"""
    Description of program: Project 2 - Algorithm Analysis 
    Filename: Project 2 - Muskan Fatima
    Author: Muskan Fatima
    Date: 2023
    Course: PROG 1353
    Assignment: Project 2
    Collaborators: -
"""
#the sequential search that looks until the end of the list to find the negative number 
def sequential_search(lst):
    for x in lst:
        if -x in lst:
            return True
    return False 
#algorithm two for the binary search
def binary_search(lst, target):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return True
        elif target < lst[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False

def contains_opposites(lst):
    i = 0
    j = len(lst) - 1
    while i < j:
        if lst[i] + lst[j] == 0:
            return True
        elif lst[i] + lst[j] < 0:
            i += 1
        else:
            j -= 1
    return False



input_sizes = [5000, 10000, 20000, 40000, 80000]
sequential_search_times = []
binary_search_times = []
contains_opposites_times = []

for n in input_sizes:
    # Generate a random list of n elements in the worst case (no pair of opposites)
    lst = sorted(random.sample(range(1, n + 1), n))

    # Time the sequential_search algorithm
    start_time = time.time()
    sequential_search(lst)
    end_time = time.time()
    sequential_search_times.append(end_time - start_time)

    # Time the binary_search algorithm
    start_time = time.time()
    for x in lst:
        binary_search(lst, -x)
    end_time = time.time()
    binary_search_times.append(end_time - start_time)

    # Time the contains_opposites algorithm
    start_time = time.time()
    contains_opposites(lst)
    end_time = time.time()
    contains_opposites_times.append(end_time - start_time)


# Print the results as a table
print("n\tSequential Search\tBinary Search\tThird Algorithm")
for i in range(len(input_sizes)):
    print(f"{input_sizes[i]}\t{sequential_search_times[i]:.6f}\t{binary_search_times[i]:.6f}\t{contains_opposites_times[i]:.6f}")



# Plot the results
plt.plot(input_sizes, sequential_search_times, label="sequential_search")
plt.plot(input_sizes, binary_search_times, label="binary_search")
plt.plot(input_sizes, contains_opposites_times, label="contains_opposites")
plt.legend()
plt.xlabel("Input size (n)")
plt.ylabel("Time (seconds)")
plt.show()


