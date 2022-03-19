class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_e =[]

        def dfs(els):
            if len(els) == 0:
                result.append(prev_e[:])

            for el in els:
                next_e = els[:]
                next_e.remove(el)

                prev_e.append(el)
                dfs(next_e)
                prev_e.pop()

        dfs(nums)
        return result
