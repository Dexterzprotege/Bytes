# Time complexity is o(n) and Space complexity is o(n)
def approach2(nums1,nums2) -> float:
    arr = []
    i = 0 ; j = 0 
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            arr.append(nums1[i])
            i+=1
        else:
            arr.append(nums2[j])
            j+=1
    while i < len(nums1):
        arr.append(nums1[i])
        i+=1
    while j < len(nums2):
        arr.append(nums2[j])
        j+=1
    # print(arr) -> debug to check if array is sorted
    n = len(arr)-1
    return findmid(arr,len(arr)-1)


def findmid(arr,n):
    return arr[n//2] if n+1&1 else (arr[n//2]+arr[(n//2)+1])/2

# Time complexity is O(n+nlogn) Space complexity is O(n)
def approach1(nums1,nums2) -> float:
    arr = nums1+nums2
    arr.sort()
    return findmid(arr,len(arr)-1)

def medianofsortedArrays(nums1,nums2) -> float:
    # return approach1(nums1,nums2)
    return approach2(nums1,nums2)



if __name__ == '__main__':
    nums1 = list(map(int,input().split()))
    nums2 = list(map(int,input().split()))
    ans = medianofsortedArrays(nums1,nums2)
    print(ans)