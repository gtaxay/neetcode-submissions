class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        adj = [[] for i in range(n)]

        # intialize adj
        for one, two in edges:
            adj[one].append(two)
            adj[two].append(one)

        # track visited nodes
        visited = set()
        count = 0
        def dfs(val):
            # base case no neighbors

            
            # add to visited then go trhouhg neighobsr
            visited.add(val)
            for nei in adj[val]:
                if nei not in visited:
                    dfs(nei)
            
            return
            

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count

            
        

        