
# Algorithm Comparison Project
# Overview
This project implements and compares three different algorithms that solve the same problem: determining if a sorted list of positive and negative integers (no zeroes) contains a value x such that both x and -x are in the list.


# The Algorithms
# Algorithm #1: Sequential Search
For each element in the list, do a sequential search to see if its negative is also in the list. Sequential search means you examine each element in the list one by one (iterate over the elements in the list).

# Algorithm #2: Binary Search
For each element in the list, do binary search to see if its negative is also in the list. Pseudo code for binary search algorithm is provided.

# Algorithm #3: Two Indices
Maintain two indices i and j, initialized to the first and last element in the list, respectively. If the two elements being indexed sum to 0, then x has been found. Otherwise, if the sum is smaller than 0, advance i; if the sum is larger than 0 then retreat j, and repeatedly test the sum until either x is found or i and j meet.

# What I did
I implemented the three algorithms.
I tested my algorithms on some pre-determined lists to verify they worked.
I analyzed the three algorithms using instruction counting to providing the big-Oh function in terms of n in the worst case. Note that the worst case happens where the answer is false.
I confirmed my analysis by timing the algorithms for different input sizes in the worst case. At a minimum, I used input sizes of: 5,000; 10,000; 20,000; 40,000, and 80,000. I presented this data in a table and graphed my results.
I graphed the results in matplotlib.
