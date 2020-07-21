

# Explanation of Active Directory Solution

 - First, I converted the input group to list type to make it iterable.
 - Then using a loop on a list created in the previous step. I checked for a vaild Group.If its not valid i returned False. Then I checked if the user is in the group of not. If yes then i returned True else checked if the group further contain sub-groups if no then I returned False I yes I recursed on the sub-group.
## Time Complexity:
 - Time complexity for a tree of n nodes (here groups) is `O(n)` and for each node there is a list of users of length `l` that we need to search for a user so the time complexity is `O(n*l)`
 

## Space Complexity:
-   `O(b*m)`  where m is the longest path and b is the number of sibling nodes along the path.

