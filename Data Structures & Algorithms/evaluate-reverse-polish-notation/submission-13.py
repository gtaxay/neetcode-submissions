class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        # stack because reverse polish notation
        # expression


        for t in tokens:

            # always valid so dont have to check two

            if t == "+":
                one, two = stack.pop(), stack.pop()
                stack.append(one + two)
            elif t == "-":
                one, two = stack.pop(), stack.pop()
                stack.append(two - one)
            elif t == "*":
                one, two = stack.pop(), stack.pop()
                stack.append(two * one)
            elif t == "/":
                one, two = stack.pop(), stack.pop()
                stack.append(int(two / one))
            else:
                stack.append(int(t))
            
        return stack[-1]
