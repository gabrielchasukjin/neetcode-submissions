class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        in_stack = set() 
        
        graph = {}

        for link in prerequisites:
            pre, post = link[0], link[1]
            if pre in graph:
                graph[pre].append(post)
            else:
                graph[pre] = [post]
        
        def dfs(node):
            if node in in_stack:
                return True
            if node in visited:
                return False 

            visited.add(node)
            in_stack.add(node)

            for neighbor in graph.get(node, []): 
                if dfs(neighbor):
                    return True
            print(node)
            in_stack.remove(node)
            return False
        res = []
        for n in range(numCourses):
            res.append(dfs(n))
        
        return not any(res)