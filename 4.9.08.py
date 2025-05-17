def print_key_val(**kwargs):
    '''
    Функция выводит переданные параметры в фиде key --> value
    '''
    for key, value in kwargs.items():
        print(f'{key} --> {value}')


print_key_val(name='Max', age=21)