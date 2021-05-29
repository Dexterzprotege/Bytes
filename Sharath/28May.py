# 28-May-2020

# 1. H-INDEX: https://leetcode.com/problems/h-index/
class Solution: #(32ms-91.13% Time) and (14.3MB-95.56% Space)
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] <= i:
                return i
        return len(citations)

# 2. Median of two sorted arrays: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Trivial Solution:
class Solution: #(100ms-26.82% Time) and (14.5MB-77.83% Space)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        arr = [0]*n
        i, j, k = 0, 0, 0
        while i<len(nums1) and j <len(nums2):
            if nums1[i] <= nums2[j]:
                arr[k] = nums1[i]
                i += 1
                k += 1
            else:
                arr[k] = nums2[j]
                j += 1
                k += 1
        while i < len(nums1):
            arr[k] = nums1[i]
            i += 1
            k += 1
        while j < len(nums2):
            arr[k] = nums2[j]
            j += 1
            k += 1
        if n%2 == 0:
            return (arr[n//2]+arr[n//2 - 1])/2
        return arr[n//2]
      
# Optimised one:
class Solution: #(96ms-43.15% Time) and (14.7MB-5.28% Space)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        X = len(nums1)
        Y = len(nums2)
        start = 0
        end = X
        partitionX = (start+end-1)//2
        partitionY = math.ceil((X+Y)/2) - partitionX - 2
        while True:
            XLeft = nums1[partitionX] if partitionX >= 0 else float("-infinity")
            XRight = nums1[partitionX+1] if (partitionX+1)<len(nums1) else float("infinity")
            YLeft = nums2[partitionY] if partitionY >= 0 else float("-infinity")
            YRight = nums2[partitionY+1] if (partitionY+1)<len(nums2) else float("infinity")

            if XLeft <= YRight and YLeft <= XRight:
                if (X+Y)%2 == 0:
                    return (max(XLeft,YLeft)+min(XRight,YRight))/2
                else:
                    return max(XLeft,YLeft)
            elif XLeft>YRight:
                partitionX -= 1
                partitionY += 1
            else:
                partitionX += 1
                partitionY -= 1
        return -1
