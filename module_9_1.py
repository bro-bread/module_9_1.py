

def apply_all_func(int_list, *functions):
    dict_def = {}
    for i in  functions:
        results = i(int_list)
        dict_def[i.__name__] = results
    return dict_def

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))