class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > n - 1:
            return False

        adj = [[] for i in range(n)]
        for one, two in edges:
            adj[one].append(two)
            adj[two].append(one)
        
        # all visited so we can track cycles
        visited = set()
        # prev is needed to not include previous number in cycle

        def dfs(val, prev):
            if val in visited:
                return False
            
            visited.add(val)
            for branch in adj[val]:
                # base case
                # if neighbor is prev
                if branch == prev:
                    continue
                if not dfs(branch, val):
                    return False
            
            return True
        
        # how to know where to start. can test all


        
        return dfs(0, -1) and len(visited) == n

        