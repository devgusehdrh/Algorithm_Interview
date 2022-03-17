def default(s):
    # 2자리 문자열, 3자리 문자열 판단 함수
    def expand(left,right):
        # 왼쪽 값이 0보다 크거나 같고 오른쪽 값이 총 문자열 길이보다 작으며, 왼쪽값 문자열과 오른쪽값 문자열이 같으면 밑의 코드를 돌린다.
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # 왼쪽값 -1 
            left -= 1
            # 오른쪽값 +1
            right += 1

        # 문자열 슬라이싱[왼쪽값+1:오른쪽값]
        # 왼쪽값에 1을 더해주는 이유는 위의 코드에서 s[1]==s[4] 일경우 리컨 값은 s[0:5] 이므로
        # s[0] 부터 s[4]까지 출력된다. 우리가 원하는 값은 s[1]부터 s[4]까지 이므로 왼쪽값에 1을 더해주어야한다.
        # 인덱스와 슬라이싱의 차이로 인함
        return s[left+1:right]
    # 문자열이 2보다 작거나 앞, 뒤로 읽어서 같다면 그대로 출력
    if len(s) < 2 and s == s[::-1]:
        return s
    # 결과값 선언
    result = ''
    # 문자열의 길이만큼 반본
    for i in range(len(s)):
        # 결과값, 2자리 문자열, 3자리 문자열 중 길이를 기준으로 가장 큰 값을 결과값에 넣는다
        result = max(result, expand(i,i+1), expand(i,i+2), key=len)
    return result



s = 'ababn'
print(default(s))