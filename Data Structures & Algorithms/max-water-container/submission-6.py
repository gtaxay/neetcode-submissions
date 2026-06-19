class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # two bars
        # start front and back
        # whichevre is lower move
                                         
        front, back = 0, len(heights) - 1

        water = 0
        while front < back:
            area = (back - front) * min(heights[front], heights[back])

            water = max(area, water)

            if heights[front] > heights[back]:
                back -= 1
            else:
                front += 1

        return water 
    
        