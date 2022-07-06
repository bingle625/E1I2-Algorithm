# N: 재료의 개수 - 신맛(S), 쓴맛(B)

class Solution:
    minV = 1000000000

    def min_diff(self, ingreds):
        # 모든 경우의 수 찾는 함수
        def find_comb(igr, s, b):
            if not igr:
                return
            
            for idx, val in enumerate(igr):
                S = s * val[0]
                B = b + val[1]
                self.minV = min(self.minV, abs(S-B))

                find_comb(igr[idx+1:], S, B)

        find_comb(ingreds, 1, 0)
        print(self.minV)

# 입력 받기
N = int(input())
ingreds = []
for _ in range(N):
    ingreds.append(tuple(map(int, input().split())))

s = Solution()
s.min_diff(ingreds)