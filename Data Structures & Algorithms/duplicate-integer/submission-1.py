class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memory = set()
        for val in nums:
            if val in memory:
                return True
            else:
                memory.add(val)
        
        return False

            
        