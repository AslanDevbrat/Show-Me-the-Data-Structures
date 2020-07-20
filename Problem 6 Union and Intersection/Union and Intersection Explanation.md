
# Explanation of Union and Intersection solution

 - I used the set data structure.

 ## Union 
- I traversed both LinkedList and stored the value in a temp_set variable, which is a  set variable. Then made the LinkedList of value present temp_set variable. Since temp_set can't have duplicate values, at last, it will create a union of two list
- **Time Complexity**: As I am traversing both the Linked one by one-time complexity is O(m+n) where m and n are the lengths of each LinkedList.
- While creating the new LinkedList in worst Time case, the complexity will be O(n+m) where m and n are the lengths of each LinkedList.
- **Space Complexity** same explanation follow O(n+m) 
## Intersection
- I traversed Both LinkedList and maintained two set variables to store the value of the respective LinkedList. Then I took the intersection of the two set variables and created the LinkedList of those values.
- **Time Complexity** Since I am looping both LinkedList at once, The time complexity will be O(n) where n is the length of the longest LinkedList.intersect operation will take O(1). In the worst case, creating a Linked list of the intersecting element will take O(n)
- **Space Complexity** O(n) similar explanation as time complexity


