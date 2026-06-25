class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        in_stack = set() 

        graph = {}
        for link in prerequisites:
            pre, post = link[1], link[0]
            if pre not in graph:
                graph[pre] = [post]
            else:
                graph[pre].append(post)
        print(graph)
        def dfs(node):

            if node in in_stack: 
                return True
            if node in visited:
                return False
            
            visited.add(node)
            in_stack.add(node)

            for neighbor in graph.get(node, []):
                if neighbor in graph and dfs(neighbor):
                    return True
            
            in_stack.remove(node)
            return False
        
        ans = []
        for course in range(numCourses):
            if course not in visited:
                ans.append(dfs(course))
        
        return not any(ans)
