def count_char(str):
    str_temp = sorted(set(list(str)))
    ans = {}
    for char in str_temp:
        ans.update({char: str.count(char)})
    return ans

string = "Happiness"
arr_count_char = count_char(string)
print(arr_count_char)