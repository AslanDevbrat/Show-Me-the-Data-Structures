_# Idea behind the code_

# Huffman Encoding:

-
# Phase 1-Build the Huffman tree

  - Generated a dictionary which contain \&lt;key,value\&gt; as \&lt;character,character\_frequency\&gt;

Time Complexity = O(n)

  - Sorted the Dictionary in reverse order based on their frequency Time Complexity = O(nlog(n))
  - Converted this Dictionary to the List

Time Complexity = O(1)

  - Inside a while loop I took the last two element and created a new node with these previous node as left and right child. And set the value of the new node to the sum of frequencies of the last two nodes. Then Appended a tuple(new\_node, new frquency) to the original list. The inside the loop itself I sorted the list based of the frequencies is reverse order. Repeated the same process till there is only one element in the List.

Time Complexity = Extracting miminum frequency from the priority queue take place 2\*(n-1) times and its complexity O(nlog n)

The over all complexity is O(n log n)

-
# Phase 1-Build the Huffman tree

  - Using recursion I traversed the whole tree in In-order DFS fashion.

if the node has left child the I appended &#39;0&#39; to the code and If it has righr child the I appended &#39;1&#39; to it.

This way I createda dictionary using this with character as key and their huffmancode as value.

Time Complexity = O(logn)

**Over Time Complexity** = O(nlog n)
**Space Complexity** = O(n)

# Huffman Decoding:

- I traversed a whole encoded string, I the one bit is 0

Then I moved the node pointer to the left child of it. If bit is 1

this I moved the node pointer to the right of it. If node points to the leaf node the I appended to the final decoded string that character .

Time Complexity = O(n)
