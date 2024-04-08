class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        ro = len(mat);
        co = len(mat[0]);
        
        if ro*co != r*c:
            return mat;
        re0 = []
        for row in mat:
            re0 = re0 +row
        re = []

        for i in range(1,r+1):
            re.append(re0[(i-1)*c:i*c])
            
        return re