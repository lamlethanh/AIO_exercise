def count_chars(string):
    dict_ans = {}
    arr_char = sorted(set(string))
    for char in arr_char:
        dict_ans.update({char: string.count(char)})
    return dict_ans


string = input()
dict_counting = count_chars(string)
print(dict_counting)
