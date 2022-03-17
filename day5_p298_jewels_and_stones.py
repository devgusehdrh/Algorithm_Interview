from collections import Counter as C

# Count 모듈 사용
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count_J = C(J)
        cnt = 0

        for i in S:
            if i in count_J:
                cnt += 1
        return cnt

# 교재 변경
from collections import Counter as C

    class Solution:
        def numJewelsInStones(self, J: str, S: str) -> int:
            count_S = C(S)
            cnt = 0

            for i in J:
                if i in count_S:
                    cnt += count_S[i]
            return cnt

# 교재
    def numJewelsInStones_in_the_book(self, J: str, S: str) -> int:

        freqs = {}
        count = 0

        for char in S:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1
        for char in J:
            if char in freqs:
                count += freqs[char]

        return count