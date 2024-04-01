class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        mm = len(ransomNote)
        for i in magazine:
            if i in dic:
                dic[i] = dic[i] + 1;
            else:
                dic[i] = 1
        for i in ransomNote:
            if i in dic:
                dic[i] = dic[i] - 1;
                mm  = mm - 1;
                if dic[i] < 0 :
                    return False;
            else:
                return False;
            
        return mm == 0