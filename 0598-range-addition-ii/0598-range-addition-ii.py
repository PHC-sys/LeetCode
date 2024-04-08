class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        mmin = m;
        nmin = n;
        for i in ops:
            #print(i)
            if i[0] < mmin:
                mmin = i[0];
            if i[1] < nmin:
                nmin = i[1];
        return mmin*nmin;