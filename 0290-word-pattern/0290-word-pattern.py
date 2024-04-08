class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        if len(s.split())!=len(pattern): return False
        dic={}
        for word in s.split():
            if not pattern[0] in dic.values() and not word in dic: dic[word]=pattern[0]
            else:
                if not word in dic or dic[word]!=pattern[0]: return False
            pattern=pattern[1:]
        return True