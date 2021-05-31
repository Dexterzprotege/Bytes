# 29-May-2021

# 1. Merge overlapping intervals - https://leetcode.com/problems/merge-intervals/
class Solution: #(88ms-46.77% Time) and (16.1MB-82.48% Space) - O(nlogn) and O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ans = []
        for interval in intervals:
            if len(ans)==0 or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans

# 2. First and last occurrence of element in sorted array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution: #(112ms-6.07% Time) and (15.6MB-8.87% Space) 
   def searchFirst(self, nums, start, end, target):
        result = -1
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                result = mid
                end = mid -1
            else:
                start = mid + 1
        return result
    def searchLast(self, nums, start, end, target):
        result = -1
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                result = mid
                start = mid + 1
            else:
                end = mid - 1
        return result

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                result.append(self.searchFirst(nums, start, mid, target))
                result.append(self.searchLast(nums, mid, end, target))
                return result
            elif nums[mid]<target:
                start = mid + 1
            else:
                end = mid -1
        return result if len(result)!=0 else [-1, -1]
    
# Approach 2:
class Solution: #(84ms-68.77% Time) and (15.6MB-8.87% Space) 
    def searchFirst(self, nums, target):
        low, high = 0, len(nums)-1
        res = -1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                res = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return res
    def searchLast(self, nums, target):
        low, high = 0, len(nums)-1
        res = -1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                res = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return res
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        result = []
        result.append(self.searchFirst(nums, target))
        result.append(self.searchLast(nums, target))
        return result if len(result)!=0 else [-1, -1]
    
# 3. H-Index II - https://leetcode.com/problems/h-index-ii/

