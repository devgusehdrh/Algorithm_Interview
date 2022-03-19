class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(els, start, k):
            if k == 0:
                result.append(els[:])
                return

            for i in range(start, n + 1):
                els.append(i)
                dfs(els, i + 1, k - 1)
                els.pop()

        dfs([], 1, k)
        return result