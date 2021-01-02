  **What is Binary Search ?**
                  
*Binary search is the most fundamental and useful searching algorithm in computer science.
It is intuitive to search any element(target) in an array by comparing each element of an array with the target element and has a time complexity of O(1).
But, can we improve the algorithm. Maybe not, knowing this target exists in the array or not, We need to compare or explore each element.
But what if we have a constraint that all items are sorted in an array. Can we improve our search algorithm?*


*Since the array is sorted, finding a target can be more efficient as We don't need to explore all the elements in an array as we know where this element can exist, which gives us the searching function as a monotonic function. In a binary search, we start our search from the middle element, and there can be three cases.* 

* If the middle element is equal to the target element, then we have found the target.

* If the target element is less than the middle element, we are sure we don't need to explore the greater elements than the middle element.

* If the target is greater than the middle element, we are confident we don't need to explore the smaller elements than the middle element.

* Do we see the pattern of how we are reducing search space every time by half? That's why the time complexity of the algorithm is O(log n).*
