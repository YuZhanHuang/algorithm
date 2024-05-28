## Selection Sort

### overview
The algorithm works by repeatedly finding the minimum element in the list and placing it at the beginning.
This way, the algorithm maintains two lists:

1. the sublist of already-sorted elements, which is filled from left to right.
2. the sublist of the remaining unsorted elements that need to be sorted.


In other words, this algorithm works by iterating over the list and swapping each element with the minimum (or maximum) element found in the unsorted list with that in the sorted list.


### Time Complexity
The time complexity of this code is in O(n^2) because finding a minimum number in the list requires 
iterating over the entire list for each element of the given list. 
The quadratic time complexity makes it impractical for large inputs.