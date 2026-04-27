class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][1]:
                index, t = stack.pop()
                sol[index] = i - index
            stack.append((i,temp))
            

        return sol
        