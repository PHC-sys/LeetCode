class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = x ^ y
        y = 0
        while x:
            print(bin(x))
            y += 1
            x = x & (x - 1)
        return y