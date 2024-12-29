#Brute Force Approach (On2)
height=[1,8,6,2,5,4,8,3,7]
maxwater=0
for i in range(len(height)):
    for j in range(i+1,len(height)):
        width=j-i
        heig=min(height[i],height[j])
        area=width*heig
        maxwater=max(maxwater,area)
print(maxwater)