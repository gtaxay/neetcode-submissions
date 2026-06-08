class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s
        return output

    def decode(self, s: str) -> List[str]:

        sol = []
        # find len, by going until #
        front, back = 0, 0
        while back < len(s):
            while s[back] != "#":
                back += 1
           
            
            length = int(s[front:back])
            sol.append(s[back + 1: back + 1 + length])
            front = back + 1 + length
            back = front
        
        return sol

                


