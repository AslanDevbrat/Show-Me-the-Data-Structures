


# Explanation of The Blockchain Solution


 - First i created a block containing index,data(transaction) , hash_of
   the previous block, time of creating the block, and nonce*.
   
 - The first block is called is genesis block. It will be the first block in every blockchain.
 - I also added proof of work that tries differeent values of hh to get a has that satisfies our difficulty criteria.
 - Once the all nodes are chanined all are stored in a chain list vairiable.
 - Then i created a LinkedList with each node containing a block.
 ## Time complexity
The proof_of_work (block) fuction is taking the most of the time to find the hash which match the difficulty lavel. If the difficulty is n (2 in my case) the Time complexity of this function is approx O(10^n) (This is the observation i got from the nonce value)
 - The check_chain_validity() take time proportional to the length of the chain
	 O(n)
 - Finally after creating the chain list it take time proportional to the lenght of the chain to make LinkedList. O(n)
 ** Overall Time Complexity = O(1)** because The time complexity of adding a single transaction is what we are looking for.
## Space Complexity = O(n)

