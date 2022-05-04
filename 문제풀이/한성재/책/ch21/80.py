import collections

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = collections.Counter(tasks)
        result = 0
        
        while True:
            sub_count = 0
        
        # 개수 순 추출 (트릭2)
            for task, _ in counter.most_common(n+1):
                sub_count += 1
                result += 1
                
                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전히 제거 굉장히 유용한 핵 (트릭1)
                counter += collections.Counter()
            
            if not counter:
                break
            
            result += n - sub_count +1
            
        return result
                