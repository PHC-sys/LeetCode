class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for i in s:
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1
        
        for i in t:
            if i not in dic:
                return i
            else:
                dic[i] = dic[i] - 1
                
        for i,v in dic.items():
            if v != 0:
                return i