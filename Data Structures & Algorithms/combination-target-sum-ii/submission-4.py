class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(index, current):
            # correct and add
            if sum(current) == target:
                res.append(current.copy())
                return
            
            # end 
            if index == len(candidates) or sum(current) > target:
                return 
            
            current.append(candidates[index])
            backtrack(index + 1, current)
            current.pop()

            while index  + 1< len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1, current)

        backtrack(0, [])
        return res

        