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
