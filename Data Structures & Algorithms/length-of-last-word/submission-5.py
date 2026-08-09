class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        words = s.split(" ")
        print(words)
        
        for i in range(len(words)-1,-1,-1):
            word = words[i]
            print(word)
            if word != "":
                return len(word) 
        
        