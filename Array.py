from array import *

arr= array('i', [5,65,34,23,22,46])

n=int(input("Enter the length of array: "))

for i in range(n):
    x=int(input("Enter the elements: "))
    arr.append(x)

print("The array elements are as follows: ")
print(arr)