def findnumIdx(nums1,num):
    for idx,ele in enumerate(nums1):
        if (ele > num) or (idx > 0 and ele < nums1[idx-1]):
            return idx
    return len(nums1)-1

def placeelement(arr,num,idx,maxlen):
    while(maxlen >= idx):
        arr[maxlen] ,arr[maxlen+1] = arr[maxlen+1],arr[maxlen]
        maxlen-=1
    arr[idx] = num

def approach1(nums1,m,nums2,n):
    if m == 0 and n!=0:
        nums1 = nums2.copy()
        return 
    for num in nums2:
        getIdx = findnumIdx(nums1,num)
        placeelement(nums1,num,getIdx,m-1)
        m+=1
    
    
def approach2(nums1,m,nums2,n):
    for i in range(m,m+n):
        nums1[i] = nums2[i-m]
    nums1.sort()


def approach3(nums1,m,nums2,n):
        arr=[0]*(m+n)
        k = 0
        i = 0;j =0
        while(i < m and j < n):
            if nums1[i] < nums2[j]:
                arr[k] = nums1[i]
                i+=1
            else:
                arr[k] = nums2[j]
                j+=1
            k+=1
        while i < m:
            arr[k] = nums1[i]
            k,i=k+1,i+1
        while j < n:
            arr[k] = nums2[j]
            k,j = k+1,j+1
        print(arr)
            

def approach4(nums1,m,nums2,n):
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]
    
def mergesortedArr(nums1,m,nums2,n):
    approach1(nums1,m,nums2,n)
    approach2(nums1,m,nums2,n)
    approach3(nums1,m,nums2,n)
    approach4(nums1,m,nums2,n)





if __name__ == '__main__':
    # nums1 = list(map(int,input().split()))
    nums1 = [1,2,4,0,0,0]
    m = 3
    # nums2 = list(map(int,input().split()))
    nums2 = [2,5,6]
    n = 3
    mergesortedArr(nums1,m,nums2,n)
    print(*nums1)
