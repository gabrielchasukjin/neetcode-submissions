class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        running = [] 

        for task in operations:

            if task == "+":
                last_two = running[-2:]
                running.append(sum(last_two))

            elif task == "D":
                last_one = running[-1:][0]
                running.append(last_one * 2)

            elif task == "C":
                running = running[:-1]

            else: 
                running.append(int(task))
        
        return sum(running)
        