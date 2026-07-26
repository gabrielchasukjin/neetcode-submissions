class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = set()
        stack = [] 

        graph = {}
        for a, b in prerequisites: 
            if a in graph.keys():
                graph[a].append(b)
            else:
                graph[a] = [b]

        def dfs(node): 
            
            if node in stack:
                return False 
            if node in visited:
                return True
            
            stack.append(node)
            
            if node in graph:
                for neighbor in graph[node]: 
                    if not dfs(neighbor):
                        return False 
            
            visited.add(node)
            stack.remove(node)

            return True
            
        
        ans = []
        for i in range(numCourses):
            if i not in visited:
                ans.append(dfs(i))
        # print(ans)
        return all(ans)
        