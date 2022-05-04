class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        
        start, fuel = 0, 0
        for i in range(len(gas)):
            #출발점이 안 되는 지점 판별
            if gas[i] + fuel < cost[i]:
                start = i +1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start
        
        # for start in range(len(gas)):
        #     fuel = 0
        #     for i in range(start, len(gas)+ start):
        #         index = i % len(gas)
                
        #         can_travel = True
        #         if gas[index] + fuel < cost[index]:
        #             can_travel = False
        #             break
                
        #         else:
        #             fuel += gas[index] - cost[index]
        #     if can_travel:
        #         return start
        # return -1