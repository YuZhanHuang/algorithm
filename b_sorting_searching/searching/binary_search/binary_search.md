## Binary Search
> Assuming that the input array is **sorted**

The key idea is simple. Assuming that the input array is **sorted**, 
compare the element that is being searched for with the element at the middle of the array. 
If the element being searched for is greater than the element at the middle of the array,
recursively check for it in the second half of the given array.
Otherwise, search for it in the first half of the given array.

### Implementation

The element to be searched is compared with the element at the middle index. 
If it matches, the index of the middle element is returned. 
If it does not match, we check if the element is greater or smaller than the middle element.

If the element is smaller than the middle element, the `left` index is accordingly updated to be `mid + 1`.
In this way, we ignore the left half of the array.

Similarly, if the element at the middle is greater than the element that we’re searching for, 
the element we’re searching for is in the initial half of the list. 
Hence, the `right` index is updated to be `mid - 1`. In this way, we ignore the right half of the array.

We iterate over the left or right half of the array by comparing the key with the middle element `mid` and 
continue iterating until the index of the search element is found, 
or the array is fully traversed in that particular half. If the required number exists, 
its index is returned. And if it does not, -1 is returned, 
indicating that the searched number does not exist.

### Performance of binary search
Binary search runs in O(log(n)). This is because the list is halved at every iteration.