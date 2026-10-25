class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # frequency = map

        # go through nums and put into map
        # reverse go through bucket


        # count frequency
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        

        
        # put into buckets
        # position is frequency i = 0 means never 
        # longest possible is nums length if all 1

        # array of arrays
        buckets = [[] for i in range(len(nums) + 1)] 

        for key, value in count.items():
            buckets[value].append(key)
        
        # reverse and output
        res = []

        for b in reversed(buckets):
            
            for v in b:
                if len(res) == k:
                    return res
                res.append(v)
        
        return res
        






        

        