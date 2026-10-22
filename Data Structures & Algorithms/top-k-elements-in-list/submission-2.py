class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        count = dict(sorted(count.items(), key=lambda x:x[1]))
        
        out = []
        for n in range(k):
            out.append(count.popitem()[0])
        
        return out