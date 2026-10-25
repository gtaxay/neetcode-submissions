class Solution:

    # need to know length of string
    # can include characters so need to know when to stop

    # 0123
    # 2#hi

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += "" + str(len(s)) + "#" + s
        
        return res


    def decode(self, s: str) -> List[str]:

        res = []

        front, back = 0, 0 

        while back < len(s):

            # get length
            while s[back] != "#":
                back += 1
            
            length = int(s[front:back])
            # back + 1 + length + 1
            res.append(s[(back + 1):(length + back + 1)])

            front = length + (back + 1)
            back = front
        
        return res

            


