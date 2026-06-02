class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # many sub problems
        # i, i + 1, i + 2 floor, ...
        # bottom up for min
        # last value is 0]
        # second to last value is cost[len(cost - 1)]

        one, two = cost[len(cost) - 1], 0

        # already have 2 variables
        for i in range(len(cost) - 2, -1, -1):

            cost[i] = cost[i] + min(one,two)
            one = cost[i]
            two = cost[i + 1]
        
        return min(one,two)




        