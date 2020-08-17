#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear [O(n)], because the loop will run as many times as needed until a's value exceeds n^3; which is increased through a linear function in the loop.


b) Quadriatic[O(n^2)], because the algorithm runs n times in the initial for loop, and then runs another for loop each time j < n.


c) Linear[O(n)], because it must call itself n - 1 times

## Exercise II

I'd perform a binary search to find the maximum height.

- initialize 'low' at 0, 'high' at n - 1, and 'mid' for the center (n//2).
- a while loop to begin the search, which will end when the ideal height is found (while low <= high):
    + mid set to half the sum of low and high
    + each loop checks if target is found, 
    + if egg breaks, high = mid 
    + elif egg unbroken, low = mid

- return mid

This should return the max height at which the egg can be dropped and not break, using the least eggs. The run-time complexity is log n for this code because of its binary search nature; we cut our search field in half each loop.


