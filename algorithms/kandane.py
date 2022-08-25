# 



def kandane(arr):
    max=0
    current_sum=0
    for i in range(len(arr)):
        current_sum=current_sum+arr[i]
        if max<current_sum:
            max=current_sum
        if current_sum<0:
            current_sum=0
    print(max)
arr=[1,-3,4,-2,-1,6]
kandane(arr)
