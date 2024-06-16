def sliding_find_max(arr, k):
    arr_temp = []
    arr_ans = []
    if len(arr) < k:
        return arr_temp
    else:
        while (len(arr) > 0):
            arr_temp.append(arr[0])
            arr.pop(0)
            if (len(arr_temp) >= k):
                arr_ans.append(max(arr_temp))
                arr_temp.pop(0)
    return arr_ans


list_input = list(map(int, input().split(' ')))
k = int(input())
arr_ans = sliding_find_max(list_input, k)
print(arr_ans)
