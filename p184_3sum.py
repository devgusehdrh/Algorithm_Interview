from typing import List



class Solution:
    # 브루트포스
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        # 첫번째는 i부터 n-2번까지 움직이기 가능
        for i in range(len(nums) - 2):
            # i가 이전 숫자랑 같다면 그냥 패스
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 두번째는 i+1부터 n-1번까지 움직이기 가능
            for j in range(i + 1, len(nums) - 1):
                # j가 이전 숫자랑 같다면 그냥 패스
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # 세번째는 j+1부터 n번까지 움직이기 가능
                for k in range(j + 1, len(nums)):
                    # k가 이전 숫자랑 같다면 그냥 패스
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    # 세 수를 합친다
                    sum = nums[i] + nums[j] + nums[k]
                    # 합이 0이라면 결과에 추가한다
                    if sum == 0:
                        result.append([nums[i], nums[j], nums[k]])

        return result

    def threeSum_pointer(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        # i는 n-2번째까지 움직일 수 있다.
        for i in range(len(nums) - 2):
            # i가 이전 숫자랑 같다면 그냥 패스
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 투포인터 최초 위치 설정(i+1, 마지막값)
            left, right = i + 1, len(nums) - 1
            # 왼쪽이 오른쪽보다 작아야한다.
            while left < right:
                # 합을 구한다
                sum = nums[i] + nums[left] + nums[right]
                # 합이 0보다 작을 경우 왼쪽값을 증가시킨다.
                if sum < 0:
                    left += 1
                # 합이 0보다 클 경우 오른쪽 값을 감소시킨다.
                elif sum > 0:
                    right -= 1
                # 합이 0일 경우 결과에 추가하고 왼쪽값==왼쪽값+1 일 경우 스킵한다.
                # 오른쪽값==오른쪽값-1 일 경우 스킵한다.
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result


if __name__ == '__main__':
    s1 = Solution()
    s = [-1, 0, 1, 2, -1, -4]
    print(s1.threeSum(s))
    print(s1.threeSum_pointer(s))

# num = [-1, 0, 1, 2, -1, -4]
# num.sort()
#
# print(num)
#
#
#
#
# for i in len(num):
#     search(num, i,i+1,i+2)
#
#
#
#
#
#
#
#
# class Solution:
#     result = []
#     def search(self,num:list[int], left:int,center:int,right:int):
#         while (num[left] + num[center] + num[right] == 0 and left < center and center < right):
#             result.append()
#             if right < len(num)-1:
#                 right ++
#             else:
#                 if center < right-1:
#                     center ++
#
#
#
