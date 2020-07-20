# Explanation of LRU Cache solution

My solution is to use the power of  OrderedDict from collections module which keep order of insertion of keys and we can change that order if required. The best part is all operations have O(1) time complexity.

We maintain our OrderedDict in such a way that the order shows how recently they were used. In the beginning, we will have least recently used and in the end, most recently used.  
If any update OR query is made to a key it moves to the end (most recently used). If anything is added, it is added at the end (most recently used/added)

For get(key): we return the value of the key that is queried in O(1) and return -1 if we don’t find the key in out dict/cache. And also move the key to the end to show that it was recently used.

For set(key, value): first, we add/ update the key by conventional methods. And also move the key to the end to show that it was recently used. But here we will also check whether the length of our ordered dictionary has exceeded our capacity, If so we remove the first key (least recently used)

## Time Complexity
Time complexity = O(1)

## Space Complexity
space complexity = O(n) where n is the size of the cache.

