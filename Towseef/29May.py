#https://leetcode.com/problems/merge-intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1],intervals[i][1])
                res[-1][0] = min(res[-1][0], intervals[i][0])
            else:
                res.append(intervals[i])
        return res
 #https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
#O(n) solution
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                break
        for i in range(len(nums)):
            if nums[len(nums)-i-1] == target:
                end = len(nums)-i-1
                break
        return [start, end]
 
