class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:



        # frequency hash map

        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        
        # bucket sort

        buckets = [[] for i in range(len(nums) + 1)]

        # how do we get value, then put key inside
        # need both value and key
        # freq.items() return tuple

        for key, value in freq.items():
            buckets[value].append(key)



        # return top k
        output = []

        for b in reversed(buckets):
            for n in b:
                if len(output) == k:
                    return output
                output.append(n)
        
        return output
