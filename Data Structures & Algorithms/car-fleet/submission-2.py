class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stat = [[] for i in range(len(position))] 
        stack = []
        for i in range(len(position)):
            stat[i] = [position[i], speed[i]]
        
        for p, s in sorted(stat)[::-1]:

            ttt = (target - p) / s

            if len(stack) == 0:
                stack.append(ttt)
            elif stack[-1] < ttt:
                stack.append(ttt)
            
            
            
        

        return len(stack)


        