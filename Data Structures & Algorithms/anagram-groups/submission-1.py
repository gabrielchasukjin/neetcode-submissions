class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        import string 
        alpha = list(string.ascii_lowercase)

        blueprint = {} 
        for i, val in enumerate(alpha):
            blueprint[val] = i

        res = {}
        for word in strs: 
            blue = [0] * 26
            for letter in word:
                blue[blueprint[letter]] += 1
            final = tuple(blue)
            if final in res:
                res[final].append(word)
            else:
                res[final] = [word]
        
        return (list(res.values()))

            
