class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:


        # customer [1,0,1,2,1,1,7,5]
        # grumpy = [0,1,0,1,0,1,0,1]


        # when there is a 1, that could be a potential start for activing the consecutive minutes 
        
        right = 0
        running_total = 0
        res = 0 

        while right < len(customers):
            temp_total = running_total
            
            if grumpy[right] == 1:
                
                if right+minutes < len(customers):
                    temp_total += sum(customers[right:(right+minutes)]) #window total
                else:
                    temp_total += sum(customers[right:len(customers)]) #window total

                temp = right + minutes

                while temp < len(customers):
                    if grumpy[temp] == 0:
                        temp_total += customers[temp]
                    temp += 1 
                
                res = max(res,temp_total)
                temp_total = running_total
            
            else:
                running_total += customers[right]
            
            right += 1 
        
        if sum(grumpy) == 0:
            res = running_total
        
        return res

            
                        




        