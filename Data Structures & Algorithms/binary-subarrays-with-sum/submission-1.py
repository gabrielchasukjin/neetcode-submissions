class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        n = len(nums) 
         
        for i in range(n):
            running_sum = nums[i]
            if running_sum == goal:
                ans += 1
            for j in range(i+1, n): 
                # nums[i:j+1]
                running_sum += nums[j]
                if running_sum == goal:
                    ans += 1
        return ans


        