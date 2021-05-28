
#Quick Sort https://practice.geeksforgeeks.org/problems/quick-sort/1

#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low < high:
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi-1)
            self.quickSort(arr, pi+1, high)
        
        
    def partition(self,arr,low,high):
        # code here
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

#Merge Sort  https://practice.geeksforgeeks.org/problems/merge-sort/1 

class Solution:
    def merge(self,arr, l, m, r): 
        L = arr[l:m]
        R = arr[m:]
        i = j = 0
        k = l
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = R[j]
                j += 1
            else:
                arr[k] = L[i]
                i += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self,arr, l, r):
        #code here
        if l < r:
            mid = (l+r)//2
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid+1, r)
            self.merge(arr, l, mid, r)


# Merge sorted Arrays https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums2[n - 1] > nums1[m - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1], nums1[m - 1] = nums1[m - 1], nums1[m + n - 1]
                m -= 1
            
        if m == 0 and n > 0 :
            nums1[:n] = nums2[:n]
        
        return nums1