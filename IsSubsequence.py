## https://leetcode.com/problems/is-subsequence/description/?envType=study-plan&id=level-1 

"""

As one might notice, we added a last touch to the above algorithm to make it faster.

Given a list of indices for a matched character, in order to find the suitable index, we could simply do the linear search as we did in the above Java implementation.

Since the list of indices is ordered, due to the process of construction, we could also apply the binary search on the list to locate the desired index faster.
As a comparison, we implemented this in the Python implementation.

Now hopefully, no one is puzzled with the keyword of binary search from the hints of the problem.

Complexity Analysis

Let ∣T∣|T|∣T∣ be the length of the target string, and ∣S∣|S|∣S∣ be the length of the source string.

Time Complexity: O(∣T∣+∣S∣⋅log⁡∣T∣)\mathcal{O}(|T| + |S| \cdot \log{|T|})O(∣T∣+∣S∣⋅log∣T∣).

First of all, we build a hashmap out of the target string, which would take O(∣T∣)\mathcal{O}(|T|)O(∣T∣) time complexity. But if we redesign the API to better fit the scenario of the follow-up question, we should put the construction of the hashmap in the constructor of the class, which should be done only once. The cost of this construction would be amortized by the following calls of string matches.

As the second part of the algorithm, we scan through the source string, and lookup the corresponding indices in the hashmap. The lookup operation in hashmap is constant.
However, to find the suitable index would take either O(∣T∣)\mathcal{O}(|T|)O(∣T∣) with the linear search or O(log⁡∣T∣)\mathcal{O}(\log{|T|})O(log∣T∣) with the binary search. To summarize, this part would be bounded by O(∣S∣⋅log⁡∣T∣)\mathcal{O}(|S| \cdot \log{|T|})O(∣S∣⋅log∣T∣).

As one can see, the second part heavily depends on the distribution of the characters in the target string. If the characters are distributed evenly, the entries in the hashmap would have a shorter list of indices, which in return would shorten the search time.
But in general, one could consider the approach with hashmap should be faster than the two-pointers approach, although their time complexities say otherwise.

Space Complexity: O(∣T∣)\mathcal{O}(|T|)O(∣T∣)

We built a hashmap that consists of the indices for each character in the target string. Hence, the size of values (indices) in hashmap would be ∣T∣|T|∣T∣. In the worst case, we might have as many keys as the values, i.e. each character corresponds to a unique index. In total, the space complexity of the hashmap would be O(∣T∣)\mathcal{O}(|T|)O(∣T∣).

"""

class Solution:


    

    def isSubsequence(self, s: str, t: str) -> bool:
        
      
        sliceDictTable = defaultdict(list)
        for index, letter in enumerate(t): 
            sliceDictTable[letter].append(index) 


        currMatch = -1 

        for letter in s: 

            if letter not in sliceDictTable: 

                return False # exit if there is not match 

                # Greedy match using binary search
                sliceList = sliceDictTable[letter]
                matchIndex = bisect.bisect_right(sliceList,  currMatch) 

                if matchIndex != len(sliceList):
                    currMatch = sliceList[matchIndex]
                else: 

                    return False       

        
        return True 
