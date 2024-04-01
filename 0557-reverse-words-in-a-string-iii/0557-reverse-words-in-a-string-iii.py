class Solution:
    def reverseWords(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])[::-1];
     