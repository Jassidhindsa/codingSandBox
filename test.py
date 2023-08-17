
from fibonacciSum import *
from maximumSubaraarysum import *
from search.binarySearch import *
from sorting.countingSort import *


if __name__ == "__main__":
   fibonacciSumVal = fibonacciSum(6);
   maxSubarrayVal = optimal_max_subarray([-1, 2, 4, -3, 5, 2, -5, 2])
   countingSortArr = countingSort([1,3,6,9,9,3,5,9])
   binarySearchVal = binary_search([1, 2,5,67,96,100], 67)


   print(fibonacciSumVal)