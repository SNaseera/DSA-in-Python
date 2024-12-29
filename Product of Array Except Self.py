nums=[1,2,3,4]
n=len(nums)
ans=[1]*n
for i in range(n):
    for j in range(n):
        if (j!=i):
            ans[i]*=nums[j]
print(ans)