class Solution:
    def validPalindrome(self, s: str) -> bool:

        left = 0 
        right = len(s)-1
        collision_l = 0
        while left < right: 
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                left += 1
                collision_l += 1
        left = 0 
        right = len(s)-1
        collision_r = 0
        while left < right: 
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                right -= 1
                collision_r += 1

        if collision_l > 1 and collision_r > 1:
            return False 
        return True

        

            
        