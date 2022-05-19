class Solution(object):
    def diffWaysToCompute(self, input):
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    # eval함수는 '4+5'에 대해 9로 return 해주는 함수
                    results.append(eval(str(l) + op + str(r)))
            return results

        if input.isdigit():
            return [int(input)]

        results = []
        for index, value in enumerate(input):
            if value in "-+*":
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index + 1:])

                # extend함수는 [1,2,3].extend([4,5]) 수행시 [1,2,3,[4,5]]가 아닌, [1,2,3,4,5]를 return 하는 함수
                results.extend(compute(left, right, value))
        return results
