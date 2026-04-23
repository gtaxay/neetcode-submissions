class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []


        for op in operations:

            # constraitsn say always oging to be 2 elements

            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        
        total = 0
        for s in stack:
            total += s
        return total
        