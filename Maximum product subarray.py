# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# SOLUTION

from os import *
from sys import *
from collections import *
from math import *

def maximumProduct(arr, n):
    # write your code here
    # Return an integer denoting the answer to the required problem 
    prefix = 1
    suffix = 1
    maxi = min(arr)

    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
        prefix = prefix * arr[i]
        suffix = suffix * arr[n-i-1]
        maxi = max(maxi, max(prefix,suffix))
    return maxi
    pass
