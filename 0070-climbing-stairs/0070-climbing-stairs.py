class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        
        num_two = int(math.floor(n/2))
        num_ways = 0
        
        def ncr(n,r):
            return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

        for i in range(num_two+1):
            num_ways += ncr(n-i, i)

        return num_ways
        