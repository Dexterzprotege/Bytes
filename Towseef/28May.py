# 1. (Search) Median of two sorted arrays: https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        resarr = [0]*(m+n)
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                resarr[k] = nums2[j]
                j += 1
            else:
                resarr[k] = nums1[i]
                i += 1
            k += 1
        
        while i < m:
            resarr[k] = nums1[i]
            i += 1
            k += 1
        
        while j < n:
            resarr[k] = nums2[j]
            j += 1
            k += 1
        mid = len(resarr)//2
        if len(resarr) == 0:
            return float("{:.4f}".format(0))
        elif len(resarr) == 1:
            return float("{:.4f}".format(resarr[0]))
        else:
            if (len(resarr)%2 == 0):
                return float("{:.4f}".format((resarr[mid-1]+resarr[mid])/2))
            else:
                return float("{:.4f}".format(resarr[mid]))
#2 https://leetcode.com/problems/h-index/
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        i = 0
        while i < len(citations) and citations[len(citations)-i-1] > i:
            i += 1
        return i
        
                
            
        
