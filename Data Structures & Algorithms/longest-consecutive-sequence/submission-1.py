class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set() 
        for val in nums:
            num_set.add(val)
        
        max_count = 0

        for key in num_set:
            count = 1
            value = key
            while value+1 in num_set:
                count+=1
                value = value + 1
            max_count = max(max_count, count)
    

        return max_count



        