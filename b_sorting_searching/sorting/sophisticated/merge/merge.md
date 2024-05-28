## Merge Sort

### Overview
Merge sort is a `recursive` `divide & conquer` algorithm that essentially divides a given list into two halves,
sorts those halves, and merges them in order.
The base case is to merge two lists of size 1 so,
eventually, single elements are merged in order; 
the merge part is where most of the heavy lifting happens.


### Time Complexity
The complexity of merge sort is O(nlog(n)).