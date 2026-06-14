class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sorted_s = "".join(sorted(s, reverse=True))

        sorted_t = "".join(sorted(t, reverse=True))


        if sorted_s == sorted_t:
            return True
        return False 
