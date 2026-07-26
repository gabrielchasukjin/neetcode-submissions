class Solution:
    def arrangeCoins(self, n: int) -> int:

        left = 1
        right = n

        # cost of k rows is k(k+1) // 2
        while left < right:
            mid = ((right-left)//2) + left +1
            # build staircase with mid rows
            cost = (mid*(mid+1))//2
            if cost > n:
                right = mid - 1
            else:
                left = mid 
        
        return left
    