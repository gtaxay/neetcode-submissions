class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        found = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            found[key].append(s)

        
        return list(found.values())
        