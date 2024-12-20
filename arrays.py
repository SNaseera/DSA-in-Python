from array import *

values=array('i',[5,7,8,9,9,6])

print(values)
print(values.buffer_info())
print(values.count(9))
print(values.typecode)
# values.reverse()
# print(values)
values[4]=2
print(values[4])
#Three methods of acessing the elements of list one by one
#1 method
for i in range(6):
    print("1 method: ",values[i])
#2 method
for i in range(len(values)):
    print("2 method: ",values[i])
#3 method
for i in values:
    print(i)

#characters we use 'u'

#Finding smallest number in array
ele=array('i',[75,65,40,90,25,-12])
# smallest_num=ele[0]
# for i in range(len(ele)):
#     if (ele[i]<smallest_num):
#         smallest_num=ele[i]
# print(smallest_num)
def smallest(ele):
    return min(ele) 
print(smallest(ele))

#Finding largest number in array
ele=array('i',[75,65,40,90,25,-12])
# largest_num=ele[0]
# for i in range(len(ele)):
#     if (ele[i]>largest_num):
#         largest_num=ele[i]
# print(largest_num)
def largest(ele):
    return max(ele) 
print(largest(ele))

#Linear Search
def linear_search(arr,target):
    for index in range(len(arr)):
        if arr[index]==target:
            return index
    return -1

arr=[2,4,7,9,53,67,8,9,3,6]
# target=8
target=1
result=linear_search(arr,target)
# print(result)
if result!=-1:
    print("Element found at index:",result)
else:
    print("Element not found in the array")


#Unique values
a=array('i',[1,5,7,8,6,1,5,2,7])
# unique_val=list(set(a))
unique_val=set(a)
print("Unique values are:",unique_val)

#Intersection of 2 arrays
first_arr=[1,8,7,3,5]
second_arr=[7,1,3,9,20]
intse=[]
for i in first_arr:
    if i in second_arr:
        intse.append(i)
print(intse)
