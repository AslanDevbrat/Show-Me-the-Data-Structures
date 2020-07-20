

# Explanation of Active Directory Solution

 - First, I converted the input group to list type to make it iterable.
 - Then using a loop on a list created in the previous step. I recursed on each item in the list until I found the user or any nothing.
 
## Time Complexity:
 - Time complexity for a tree of n nodes (here groups) is `O(n)` and for each node there is a list of users of length `l` that we need to search for a user so the time complexity is `O(n*l)`
 

## Space Complexity:
-   `O(b*m)`  where m is the longest path and b is the number of sibling nodes along the path.

