#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#time complexty O(n)
#space complexty O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        low = 0
        hi = len(nums)-1
        while low <= hi:
            mid = (low+hi)//2
            if mid < len(nums)-1:
                if nums[mid] > nums[mid+1]:
                    return nums[mid+1]
                elif nums[mid] <= nums[mid+1]:
                    if nums[mid] > nums[len(nums)-1]:
                        low = mid + 1
                    else:
                        hi = mid - 1
        return nums[0]
