class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counter = {}
        ans = 0
        for right in s: 
            if right in counter:
                counter[right] += 1
            else:
                counter[right] = 1 
            
            #check k rule
            max_counter = max(list(counter.values()))
            total = sum(list(counter.values()))
            remaining = total-max_counter 
            
            while remaining > k and left < len(s):
                counter[s[left]] -= 1
                left += 1
                max_counter = max(list(counter.values()))
                total = sum(list(counter.values()))
                remaining = total-max_counter 
                
            ans = max(ans, total)
        
        return ans
        