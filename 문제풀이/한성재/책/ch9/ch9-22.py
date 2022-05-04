# 22번 일일 온도

# 풀이 1 스택 값 비교


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            # 현재 온도가 스택 값보다 높다면 정답처리
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer


answer = Solution()
print(answer.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
