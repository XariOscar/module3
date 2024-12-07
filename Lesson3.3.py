def print_params(a = 1, b = 'string', c = True):
    print(a, b ,c)
print_params()
print_params(2)
print_params(2, 'Urban')
print_params(2, 'Urban', False)

print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [3, 'str', True]
values_dict = {'a': 4, 'b': 'hello', 'c': 0.2}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['msg', True]

print_params(*values_list_2, 42)






