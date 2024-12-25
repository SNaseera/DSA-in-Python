#Time Complexity O(n2)
n=4
nums=[2,7,11,15]
target=9
for i in range(n):
    for j  in range(i+1,n):
        if(nums[i]+nums[j]==target):
            print(i,j)
        
#Time Complexity O(n)
n=4
nums=[2,7,11,15]
target=18
i=0
j=n-1
ans=[]
while(i<j):
    pairsum=nums[i]+nums[j]
    if (pairsum>target):
        j-=1
    elif (pairsum<target):
        i+=1
    else:
        ans=[i,j]
        break
print(ans)

#Majority element in brute force approch

def majele(n,nums):
    for i in nums:
        frequency=0
        for j in nums:
            if (j==i):
                frequency+=1
        if (frequency>n//2):
            return i
nums=[2,2,1,1,1,2,2]
n=len(nums)
result=majele(n,nums)
print(result)

