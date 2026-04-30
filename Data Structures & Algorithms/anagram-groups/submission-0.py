class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # brute force

        res = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        
        return list(res.values())
        