class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        front, back = 0, len(numbers) - 1

        while front < back:
            total = numbers[front] + numbers[back]
            if total == target:
                return [front + 1, back + 1]
            elif total < target:
                front += 1
            else:
                back -= 1
        