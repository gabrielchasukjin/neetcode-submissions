class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        left = 0 

        for right in range(len(t)):

            if left >= len(s):
                break 

            if left < len(s) and s[left] == t[right]:
                left += 1
        
        if left == len(s):
            return True
        return False
