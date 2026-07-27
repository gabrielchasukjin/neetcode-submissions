class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {} 
        for a, b in prerequisites: 
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]

        visited = set()
        stack = [] 
        ans = []

        def dfs(node):
            if node in stack:
                return False 
            if node in visited:
                return True 

            stack.append(node)
            if node in graph:
                for neighbor in graph[node]:
                    if dfs(neighbor) == False: 
                        return False
            
            stack.remove(node)
            visited.add(node)
            ans.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return ans

        
        