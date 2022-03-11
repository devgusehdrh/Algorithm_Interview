# collections.defaultdict 호출을 위해 import
import collections

strs = ["eat","tea","tan","ate","nat","bat"]

class Solution:
    # strs 변수 정적 타입 선언(리스트[스트링]) -> 리턴 타입 결정 리스트[리스트[스트링]]
    def groupAnagrams(self,strs: list[str]) -> list[list[str]]:
        # 결과값을 받을 변수를 선언한다(기본 키값을 list로 선정)
        # 키값을 설정 안할 경우 접근하면 KeyError를 출력한다.
        result = collections.defaultdict(list)

        # strs에서 한 단어씩 정렬 시작
        for item in strs:
            # result['정렬한 단어를 합친다(키로 사용)']
            # 위의 키값에 item에 해당하는 단어를 저장
            # 반복하게 되면 고정된 키
            # ex> 'aet' 와 같은 하나의 키에 'ate' 'eat' 와 같이 여러 값이 저장된다.
            result[''.join(sorted(item))].append(item)
        return result.values()

s1 = Solution()
print(list(s1.groupAnagrams(strs)))


