
def print_params(a=1, b='string', c=True):
    print(a, b, c)

    print_params()
    print_params(2, 'string', False)
    print_params(28, 'Urban')
    print_params(13)
    print_params(b=25)
    print_params(c=[1, 2, 3])

    values_list = [10, 'BARCA', True]
    values_dict = {'a': 20, 'b': 'Real', 'c': False}
    print_params(*values_list)
    print_params(**values_dict)
    
    values_list_2 = [54.32, 'Строка']
    print_params(*values_list_2, 42)