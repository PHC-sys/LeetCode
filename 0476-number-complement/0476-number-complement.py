class Solution:
    def findComplement(self, num: int) -> int:
        """
        :type num: int
        :rtype: int
        """
        cc = len(str(bin(num))[2:]);
        return 2**cc-num-1;