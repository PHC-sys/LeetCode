class Solution:
    def isUgly(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        while n>1:
            if n%2!=0 and n%3!=0 and n%5!=0: return False
            else: n/=[i for i in (2,3,5) if n%i==0][-1]
        return n==1