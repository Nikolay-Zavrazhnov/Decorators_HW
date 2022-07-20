from Decorators_HW.my_functions.my_some_functions import summation, ListGENERATOR

file_log = 'files_log/log_function.log'
some_list = [1, ['abc'], 2, True]

summation(442, 10)

for element_gen in ListGENERATOR(some_list):
    print(element_gen)
