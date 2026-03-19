def reversearay(arr,n,i,temp):
    if i >= n/2:
        return 
    temp = arr[i]
    arr[i] = arr[n-i-1]
    arr[n-i-1] =  temp 
    return reversearay(arr,n,i+1,temp)


arr = [1,2,3,4,5,6,7]
n = len(arr)
i = temp = 0
print("Before reversing the array",arr)
reversearay(arr,n,i,temp)
print("After reversing the array",arr)
