# To find the max and second max value in an array

arr = [1, 2, 3, 3, 5, 7, 4]
max_num = arr[0]
s_max = arr[0]
for i in range(1, len(arr)):
    if arr[i] > max_num:
        s_max = max_num
        max_num = arr[i]
    else:
        if arr[i] > s_max and arr[i] < max_num:
            s_max = arr[i]
    
print(max_num, s_max)