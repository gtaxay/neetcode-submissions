class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # max water
        # two pointers
        # back and front
        # move in shorter

        # height = min(of both)
        # width = back - front

        front, back = 0, len(heights) - 1
        area = min(heights[front], heights[back]) * (back - front)

        while front < back:

            if heights[front] < heights[back]:
                front += 1
            else: 
                back -= 1

            total = min(heights[front], heights[back]) * (back - front)
            area = max(total, area)

        return area



        