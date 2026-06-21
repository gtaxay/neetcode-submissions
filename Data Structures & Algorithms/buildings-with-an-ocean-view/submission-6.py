class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        stack = []

        # stack because monotoic, like cars
        # iterate left to right and remove when blocker

        for i, h in enumerate(heights):
            # get rid of shorter buildings before
            while stack and heights[stack[-1]] <= h:
                stack.pop()

            stack.append(i)
        
        return stack
        