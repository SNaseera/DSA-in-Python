n=5
arr=[1,2,3,4,5]
for st in range(n):
    for end in range(st,n):
        for i in range(st,end+1):
            print(arr[i],end="")
        print(end=" ")
    print()

#maximum subarray sum
n=5
arr=[1,2,3,4,5]
max_sum=0
for st in range(n):
    currsum=0
    for end in range(st,n):
        currsum+=arr[end]
        max_sum=max(currsum,max_sum)
print("maximum subarray sum:",max_sum)
