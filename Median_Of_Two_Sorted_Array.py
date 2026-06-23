class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = nums1 + nums2
        lst.sort()

        n = len(lst)
        
