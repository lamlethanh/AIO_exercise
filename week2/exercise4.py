def levenshtein(string1, string2):
    if (len(string1) == 0):
        return len(string2)
    if (len(string1) > len(string2)):
        return levenshtein(string2, string1)

    # 'previous' is used to save levenshtein distance between first i elements in string2 and first j-th elements in string1
    previous = range(len(string2)+1)
    for i, value1 in enumerate(previous):
        # 'current' is used to count calculate levenshtein distance between first i elements in string2 and first j-th elements in string1
        current = [i + 1]
        for j, value2 in enumerate(current):
            insert_cost = previous[j+1] + 1
            delete_cost = current[j] + 1
            substitution = current[j] + (value1 != value2)
            current.append(min(insert_cost, delete_cost, substitution))

        # Update 'previous' after finish calculating 'current'
        previous = current

    return previous[-1]


string1 = input()
string2 = input()
print(string1, string2)
