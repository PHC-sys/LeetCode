class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort() # greed factor of each child 
        s.sort() # candy
        idxs = 0
        gi = 0
        si = 0 
        if len(s) == 0 or len(g) == 0:
            return 0;
        while si < len(s) and gi < len(g): 
            if s[si] >= g[gi]: # if current candy great than greed factor
                gi += 1 # take the candy.
            si += 1 # else just update the child.
            
        return gi