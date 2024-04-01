class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n <= 0:
            return False
        xx = str(bin(abs(n)-1));
        # print(xx)
        for i in xx[2:]:
            if i == '0':
                return False
        
        return True