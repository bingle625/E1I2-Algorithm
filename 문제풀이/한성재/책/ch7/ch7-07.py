# 두수의 합

from html import entities


def findCoup(nums: list, target: int) -> list:

    # in을 이용한 탐색 560ms
    # for i, v in enumerate(li):
    #     complement = target - v

    #     if complement in li[i+1:]:
    #         return [i, li.index(complement)]

    # # 첫 번째 수를 뺀 결과 키 조회
    # nums_map = {}

    # for i, num in enumerate(nums):
    #     # 키와 값을 바꿔서 딕셔너리로 저장
    #     nums_map[num] = i
    #     print(nums_map)

    # for i, num in enumerate(nums):
    #     if target - num in nums_map and i != nums_map[target-num]:
    #         return [i, nums_map[target-num]]

    # # 위 풀이 for문 간소화
    # nums_map = {}
    # for i, num in enumerate(nums):
    #     if target - num in nums_map:
    #         return [nums_map[target-num], i]

    #     nums_map[num] = i

    # # 투 포인터 이용
    # # 그러나 이 경우는 input 배열이 미리 배열 되어 있다는 가정 하에 푼 풀이이므로,
    # # 코딩테스트에서 풀이로 쓰이기에는 적합하지 않다.
    # left, right = 0, len(nums)-1

    # while left != right:
    #     if nums[left]+nums[right] < target:
    #         left += 1
    #     elif nums[left]+nums[right] > target:
    #         right -= 1
    #     else:
    #         return [left, right]


nums = [2, 7, 11, 15]
target = 9

print(findCoup(nums, target))
