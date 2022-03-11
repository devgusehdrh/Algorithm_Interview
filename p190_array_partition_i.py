class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 오름차순 정렬
        nums.sort()
        result = 0
        for i, n in enumerate(nums):
            if i % 2 == 0:
                result += n
        return result