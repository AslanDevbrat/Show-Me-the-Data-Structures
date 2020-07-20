# Explanation of file recursion solution

 - First I checked if the the suffix to be found is valid or not. If its valid then 		continue othewise return a list with Invalid syntax in it
 - Then checked of the give the file is a file
	 - If yes then, does it ends with the provided suffix:
		 - if yes Then I appended that path to the paths_list List
		 - If no, Then return
	 - if no , the return
 - Then iterated to the list of directories contain in the given path. And used reccursion on the provided path appended with the list item 
 - At last returned the Paths_list
## NOTE:
The paths_list is a global variable, Therefore before every call to the find_file()
you need to clear the paths_list .
## Time complexity
O(n*m) ; Where n is the number of directories and m is number of sub-directories
## Space Complexity
O(n * m) -> We need an array of size m for each folder (n)

