def radix_sort(arr):
    max_value=max(arr)
    pos=1
    while max_value // pos > 0:
        counting_sort(arr,pos)
        pos= pos*10
def counting_sort(arr, pos):
    n = len(arr)
    count = [0] * 10
    output = [0] * n
    for i in arr:
        index = (i // pos) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i]= count[i] + count[i - 1]
    for num in reversed(arr):
        index = (num // pos) % 10
        output[count[index] - 1] = num
        count[index]= count[index] -  1
    for i in range(n):
        arr[i] = output[i]
def printarray(arr):
    for i in arr:
        print(i, end=" ")
n=int(input("enter the number of elements:"))
arr=[]
for i in range(n):
    arr.append(int(input()))
radix_sort(arr)
printarray(arr)
