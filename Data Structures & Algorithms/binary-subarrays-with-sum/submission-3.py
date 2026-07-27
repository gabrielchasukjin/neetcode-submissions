class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        n = len(nums)       
        for i in range(n):
            running_sum = 0
            
            for j in range(i, n): 
                running_sum += nums[j]
                if running_sum == goal:
                    ans += 1
                elif running_sum > goal:
                    continue
        
        return ans
        