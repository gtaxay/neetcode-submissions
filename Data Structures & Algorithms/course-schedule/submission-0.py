class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        need = defaultdict(list)

        for post, pre in prerequisites:
            need[post].append(pre)

        # a value having empty [] means it does not have any prereqs
        # no prereqs is base case

        visited = set()
        def dfs(val):

            if val in visited:
                return False

            if need[val] == []:
                return True
            
            visited.add(val)
            for pre in need[val]:
                if not dfs(pre):
                    return False
            visited.remove(val)

            need[val] = []
            return True

        for start in range(numCourses):
            if not dfs(start):
                return False
            
        return True
        