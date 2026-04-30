class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # check edge case if s1 is greater than s2. s1 would never be inside of s2
        if len(s1) > len(s2):
            return False

        # intialize 26 values to zero
        s1Count, s2Count = [0] * 26, [0] * 26
        left = 0

        # intialize both arrays with all characters and their frequency
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # intialize starting total number of matches
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        # start r at len(s1) so the first window is of size s1
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # adjust index of new char
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1

            # adjust matches based on new index
            # if creates a match add 1
            # if new index is one greater then remove match
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            # adjust matches and remove based off leftmost index
            index = ord(s2[left]) - ord('a')
            s2Count[index] -= 1

            if s1Count[index] == s2Count[index]:
                matches += 1
            if s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            left += 1
        
        return matches == 26



    
        