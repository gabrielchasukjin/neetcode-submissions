class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() 

        print(people)

        left = 0 
        right = len(people)-1

        output = 0 

        while left <= right :

            if left == right:
                output += 1
                left += 1 

            elif people[right] == limit:

                right -= 1
                output += 1
            
            elif people[left] + people[right] <= limit:

                left += 1 
                right -= 1 
                output += 1
            
            else: 

                right -= 1 
                output += 1
            
                
        return output
        



