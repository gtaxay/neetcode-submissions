class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # set all values to zero

        sol = [0 for _ in range(len(temperatures))]

        stack = []

        for i, t in enumerate(temperatures):

            # while top stack less remove rest and input into sol

            while stack and stack[-1][1] < t:
                index, temp = stack.pop()
                sol[index] = i - index
            
            stack.append((i,t))
        
        return sol

        