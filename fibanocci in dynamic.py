n=int(input("Enter the fibanocci num"))
arr=[0,1]
def func(num):
    for i in range(2,n+1):
        a=arr[i-2]+arr[i-1]
        arr.append(a)
    return arr[num]
print(func(n))
