## Insertion Sort

### Overview
Insertion sort is another famous sorting algorithm and works the way you would naturally sort in real life.

It iterates over the given list, figures out what the correct position of every element is, and inserts it there.

### Time Complexity
The algorithm is O(n^2), which, again, makes it a poor choice for large input sizes. However, notice that the complexity is actually n^2
only when the input list is sorted in reverse. So, the ‘best-case’ complexity (when the list is sorted in the correct order) is 
Ω(n).

### Space Complexity
Also, note that all of these algorithms are in-place, hence their space complexity is in O(1).
