class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # front, back

        # if need smaller decrease
        # if need larger increase

        front, back = 0, len(numbers) - 1
        while front < back:
            if numbers[back] + numbers[front] < target:
                front += 1
            elif numbers[back] + numbers[front] > target:
                back -= 1
            else:
                return [front + 1, back + 1]


        