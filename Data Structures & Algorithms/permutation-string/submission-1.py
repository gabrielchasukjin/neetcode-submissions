class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False 
        
        len_s1=len(s1)
        for left in range(len(s2)-len(s1)+1):

            window = s2[left:left+len_s1]
            if "".join(sorted(s1)) == "".join(sorted(window)):
                return True

        return False
        