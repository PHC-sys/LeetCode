class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        cc1 = collections.Counter(nums1);
        cc2 = collections.Counter(nums2);
        re = [];
        for i,v in (cc1&cc2).items():
            for j in range(v):
                re.append(i)
        return re