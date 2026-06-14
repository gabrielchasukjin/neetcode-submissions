class Solution:

    def encode(self, strs: List[str]) -> str:
        # before each word, input length and "#"

        output = ""

        for word in strs:
            length = str(len(word))
            output+= length+"#"+word
        
        return output

    def decode(self, s: str) -> List[str]:

        # use while loop
        # loop until i has reached the end 
        # its possible that the numbers can be double digits, even triple digist
        # but its guaranteed that the the econding starts with digits
        # iterate i until we locate #, all letters up until the designated length will be considered a word
        
        i = 0 
        tracker = ""
        result = []
        while i < len(s):

            # if its digit check if the next word is also a digit
            # else ensure the element is "#" 
                # since we are at a key checkpoint "#"
                # we know that all elements starting from next elemenet all the way to designated length is a valid word to decode
                # we move i to the end of designated length

            if s[i].isdigit():
                print(s[i])
                tracker += s[i]
                i += 1
            
            else:
                jump = int(tracker)
                tracker = ""
                end_of_word = s[i+1:i+1+jump]
                result.append(end_of_word)
                i+=jump+1
        
        return result

                # 3#cat4#
                # 0123456


            

    