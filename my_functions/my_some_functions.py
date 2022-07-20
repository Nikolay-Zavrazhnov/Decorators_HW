from Decorators_HW.module_decorators.DECORATORS import logger2
from Decorators_HW.module_decorators.DECORATORS import logger

file_log = 'files_log/log_function.log'


@logger2(file_log)
def summation(a, b):
    return a + b


@logger2(file_log)  # функция из предыдущего ДЗ
def ListGENERATOR(any_list):
    for item in any_list:
        if isinstance(item, list):
            for inside_item in item:
                yield inside_item
        else:
            yield item
