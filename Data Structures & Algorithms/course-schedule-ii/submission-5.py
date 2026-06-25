class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {}
        for course, pre in prerequisites: 
            if course in graph: graph[course].append(pre)
            else: graph[course] = [pre]
        
        visited = set()
        in_stack = set() 
        order = []

        def dfs(node):

            if node in in_stack:
                return False
            if node in visited:
                return True
            
            in_stack.add(node)
            
            for neighbor in graph.get(node, []):
                if not dfs(neighbor):
                    return False

            in_stack.remove(node)
            visited.add(node)
            order.append(node)

            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        return order


