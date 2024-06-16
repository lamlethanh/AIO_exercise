def count_string(file):
    dict_temp = {}
    for line in file:
        arr_string = sorted(line.split())
        for string in arr_string:
            if string not in dict_temp.keys():
                dict_temp.update({string: 1})
            else:
                dict_temp[string] += 1
    sorted_keys = sorted(dict_temp)
    dict_ans = {key: dict_temp[key] for key in sorted_keys}
    return dict_ans


link = "C:\\Python\\AIO2024\\AIO_exercise\\week2\\P1_data.txt"
f = open(link, "r")
dict_ans = count_string(f)
print(dict_ans)
