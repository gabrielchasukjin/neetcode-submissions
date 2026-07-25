class Solution:
    def arrangeCoins(self, n: int) -> int:


        i = 1 
        counter = 0 

        while i <= n:

            n = n-i
            i+=1
            counter +=1
        
        return counter 