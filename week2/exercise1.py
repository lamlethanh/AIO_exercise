def func_sliding(arr):
    length = len(arr)
    arr_temp = []
    list_return = []
    while length != 0:
        arr_temp.append(arr[0])
        arr.pop(0) 
        length-=1
        if (len(arr_temp) == 3):
            list_return.append(max(arr_temp))
            arr_temp.pop(0)
    return list_return


num_list = list(map(int, input().split(' ')))
list_after_sliding = func_sliding(num_list)
print(list_after_sliding)

