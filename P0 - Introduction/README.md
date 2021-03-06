Time complexity analysis
========================

Task0: O(n), performed two iterations, where n is the size of texts or calls, whichever is larger

Task1: O(n), performed list iterations of size n twice, that's O(2n) and constant number of operations in each iteration, since set::add is O(1)

Task2: O(n), performed a single iteration of list size n and constant number of operations in each iteration

Task3: O(nlogn) 
 - performed a single list iteration of size n, that's O(n)
 - used a data structure set to remove duplications, that's O(1) because of hashing in set
 - sorting was used at last to print output in lexicographic order , that's O(nlogn)

Task4: O(nlogn)
 - a list iteration of size n 3 times, that's O(n)
 - used a data structure set to remove duplications, that's O(1) because of hashing in set
 - sorting was used at last to print output in lexicographic order , that's O(nlogn)
 
