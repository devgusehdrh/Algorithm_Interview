
# 슬라이딩 윈도우
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 최대값 초기화
        max_length = 0
        # 시작 포인터 초기화
        start = 0
        # 사용된 문자열 해시맵
        used = {}

        for idx, val in enumerate(s):
            # 값이 사용된 문자열이고 시작 포인터가 인덱스 보다 작거나 같으면 시작포인터를 1만큼 올린다
            if val in used and start <= used[val]:
                start = used[val] + 1
            # 값이 사용되지 않았다면 최대 길이와 인덱스 - 시작 포인터 + 1 을 비교하여 최대값을 저장한다
            else:
                max_length = max(max_length, idx - start + 1)
            # 사용된 물자열을 키로 설정하여 인덱스를 저장한다
            used[val] = idx
        return max_length



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 최대값 초기화
        cnt = 0
        # 시작 포인터 초기화
        left_cur = 0
        # 사용된 문자열 해시맵
        used = {}

        for right_cur, val in enumerate(s):
            # 값이 사용된 문자열이고 시작 포인터가 인덱스 보다 작거나 같으면 시작포인터를 1만큼 올린다
            if val in used and left_cur <= used[val]:
                left_cur = used[val] + 1
                print('left_cur', right_cur, ' ', left_cur)
            # 값이 사용되지 않았다면 최대 길이와 인덱스 - 시작 포인터 + 1 을 비교하여 최대값을 저장한다
            else:
                cnt = right_cur - left_cur + 1
                print('max_length', right_cur, ' ', cnt)
            # 사용된 물자열을 키로 설정하여 인덱스를 저장한다
            used[val] = right_cur
            print('used[', val, '] ', right_cur, '\n')

        return cnt