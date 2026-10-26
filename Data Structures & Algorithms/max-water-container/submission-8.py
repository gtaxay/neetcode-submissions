class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two bars, two pointers
        # brute force is n^2, go through all
        # two pointers, one in front, one in back
        # keep max water variable
        # increase/decrease pointer while the other one is shorter
        # water is min height times distance

        water = 0

        left, right = 0, len(heights) - 1

        while left < right:

            water = max(water, min(heights[left],heights[right]) * (right - left))

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return water


        