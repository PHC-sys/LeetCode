class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        ss = collections.Counter(s);
        sumx= 0 ;
        flag = 0
        for i,v in ss.items():
            if v % 2 == 0:
               sumx= sumx+ v
            if v % 2 == 1:
                flag = 1;
                sumx = sumx + (v-1)
        return sumx+1*flag