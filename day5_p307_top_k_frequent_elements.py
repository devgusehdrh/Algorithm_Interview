from collections import Counter as C

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = C(nums)
        result = []
        for i in range(k):
            result.append(max(freqs,key=freqs.get))
            del freqs[max(freqs,key=freqs.get)]
        return result



