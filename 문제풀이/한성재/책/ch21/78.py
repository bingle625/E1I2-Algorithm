class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices) - 1))
        # result = 0
        # for i in range(len(prices) -1 ):
        #     if prices[i + 1] > prices[i]:
        #         result += prices[i+1] - prices[i]
        # return result
                                                                                                                                                                       // examine whether this problem is solved.     if(ar[n] >= 0)    {         return ar[n]
                                                                                                                                                                                                                                       }     if(n == 0)    {        q   = 0
                                                                                                                                                                                                                                                            }     else     {        q   = REVENUE
                                                                                                                                                                                                                                                                         for(i=1
                                                                                                                                                                                                                                                                              i <= n
                                                                                                                                                                                                                                                                              i + +)        {             // if the length of a rod is over the maximum revenue.             if(i >= PMAX)            {                r   = PMAX - 1
                                                                                                                                                                                                                                                                                                                                                                                                    }             else             {                r   = i - 1
                                                                                                                                                                                                                                                                                                                                                                                                                                   }             // call itself recursively to solve subproblems            q   = max(q, p[r] + memoized_cut_rod(p, n - i, ar))
                                                                                                                                                                                                                                                                                            }   }    ar[n]   = q
                                                                                                                                                                       // save the result at this level.     return q
                                                                                                                                                                       }
