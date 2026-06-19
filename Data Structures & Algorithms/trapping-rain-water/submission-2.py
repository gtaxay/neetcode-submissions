class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0 for i in range(len(height))]
        right = [0 for i in range(len(height))]

        left[0] = height[0]
        right[len(height) - 1] = height[len(height) - 1]

        for i in range(1, len(height)):
            if height[i] > left[i - 1]:
                left[i] = height[i]
            else:
                left[i] = left[i - 1]

        for i in range(len(height) - 2, -1, -1):
            if height[i] > right[i + 1]:
                right[i] = height[i]
            else:
                right[i] = right[i + 1]     
        
        total = 0
        print(right)
        print(left)

        for i in range(len(height)):
            if height[i] < left[i] and height[i] < right[i]:
                total += min(right[i], left[i]) - height[i]
        
        return total
        
