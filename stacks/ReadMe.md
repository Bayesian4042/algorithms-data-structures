**What is Stack?**

*A stack is a way to store data in LIFO style(Last in, first out). The order in which data arrives becomes vital in the stack. The element inserted last is the first one to be deleted. A pile of plates in a cafeteria is a good analogy of a stack data structure. The plates are added to the stack as they are cleaned, and they are placed on the top.*


*To implement LIFO algorithm, stack has two operations push and pop. Push insert a new element at the top and pop deletes the element from the top of the stack in O(1) time.*


*One of the pattern to add for problem solving using stack is finding nearest greater/smaller elements. Let's discuss stock span problem available on leetcode to understand it better, here we need to find all the continuous smaller element for the current ith element. Continuous from i-1  element to 0 index element.*


*We can use a stack for such problems since we can keep adding a new element if it is smaller than the stack's top element. Whenever the current element is greater, we pop all the elements until we find the greater element than the current element. Let see the code in python.*
