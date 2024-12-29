def BinarySear(arr):

    n=len(arr)
    start=0
    end=n-1
    target=12
    while(start<=end):
        mid=(start+end)//2
        if(target>arr[mid]):
            start=mid+1
        elif(target<arr[mid]):
            end=mid-1
        else:
            return mid
    return -1
arr=[-1,0,3,4,5,9,12]
print(BinarySear(arr))
