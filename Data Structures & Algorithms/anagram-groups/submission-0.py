class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {} 

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in groups.keys():
                groups[sorted_word] = [word]
            elif sorted_word in groups.keys():
                groups[sorted_word].append(word)
        
        result=[]
        for group in groups.values():
            result.append(group)
        return result

        