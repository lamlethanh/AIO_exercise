def count_string(file):
    ans = {}
    for line in file:
        str_temp = list(line.split(' '))
        for word in str_temp:
            if word not in ans:
                ans.update({word: 1})
            else:
                ans[word] += 1
    return ans


def sort_dict(dict):
    my_keys = list(dict.keys())
    my_keys.sort()
    sorted_dict = {i: dict[i] for i in my_keys}
    return sorted_dict


filepath = 'C:\\Python\\AIO2024\\AIO_exercise\\week2\\P1_data.txt'
f = open(filepath, 'r')
file = f.readlines()
for i in file:
    print(i)

arr_count_string = count_string(file)
arr_count_string = sort_dict(arr_count_string)

print(arr_count_string)
