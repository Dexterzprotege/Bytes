#   optimal approach time complexity is O(NlogN+logN)
#   space complexity is O(N) -> used internally when sorting
def hIndex(citations) -> int:
    citations.sort()
    n = len(citations)
    lo,hi = 0,n-1
    while lo <= hi:
        mid = lo+(hi-lo)//2
        if citations[mid] == n-mid:
            return citations[mid] 
        if citations[mid] <= n-mid:
            lo = mid+1
        else:
            hi = mid-1
    return n-lo 



if __name__ == '__main__':
    citations = list(map(int,input().split()))
    ans = hIndex(citations)
    print(ans)
