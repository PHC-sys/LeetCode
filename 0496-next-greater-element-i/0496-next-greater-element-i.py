class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        re = [-1 for _ in nums1];
        for i,v in enumerate(nums1):
            idx = nums2.index(v)
            for j in range(idx,len(nums2)):
                print(nums2[j],v)
                if nums2[j] > v:
                    re[i] = nums2[j]
                    break;
        return re