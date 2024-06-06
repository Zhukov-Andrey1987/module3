def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(2, 'пульс')
print_params('новая', 5, False)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params()

values_list = [56, 'type', True]
values_dict = {'a': 45, 'b': 'sroka', 'c': False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [37, 'snova']
print_params(*values_list_2, 42)
