# 27-May-2021

# 1. Quick Sort - https://practice.geeksforgeeks.org/problems/quick-sort/1

class Solution:
    def quickSort(self,arr,low,high):
        if low < high:
            j = self.partition(arr, low, high)
            self.quickSort(arr, low, j-1)
            self.quickSort(arr, j+1, high)
    
    def partition(self,arr,low,high):
        pivot = arr[low]
        i = low
        j = high
        while i < j:
            while i < high and arr[i] <= pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[j], arr[low] = arr[low], arr[j]
        return j

# 2. Merge Sort - https://practice.geeksforgeeks.org/problems/merge-sort/1#

class Solution:
    def merge(self,arr, left, mid, right): 
        left_arr = arr[left:mid+1]
        right_arr = arr[mid+1:right+1]
        i, j, k = 0, 0, left

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
        
    def mergeSort(self, arr, low, high):
        #code here
        if low >= high:
            return

        mid = (low + high)//2
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid + 1, high)
        self.merge(arr, low, mid, high)

  # 3. Merge Sorted Arrays - https://leetcode.com/problems/merge-sorted-array/
  
  class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m+n-1
        i, j = m-1, n-1

        while last>=0:
            if j<0 or (i>=0 and nums1[i]>=nums2[j]):
                nums1[last]=nums1[i]
                i-=1
            else:
                nums1[last]=nums2[j]
                j-=1
            last-=1
        return nums1
