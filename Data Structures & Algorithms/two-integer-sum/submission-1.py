class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

            
        # corresponding = target - num 
        # num is the value that we are curr iterating through 
        seen = {}
        for i in range(len(nums)): 

            corresponding = target - nums[i]

            if corresponding in seen:

                return [seen[corresponding], i]
            
            seen[nums[i]]= i
        

            


        