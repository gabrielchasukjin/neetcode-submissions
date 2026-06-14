class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # brute force method --> take i
            # then take j --> O(n^2)
        
        # find all beginning sequences and build from there
        # if num-1 dne, we know its a beggining of a sequence 

        potential = []

        num_set = set(nums)

        for num in num_set:
            if num-1 not in num_set:
                potential.append(num)
        
        longest = 0

        for n in potential: 
            i = 1
            while n+i in num_set:
                i+=1 
            if i > longest:
                longest = i
        
        return longest


        