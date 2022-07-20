import datetime


def logger(some_function):  # Декоратор для задния №1

    def write_fun(*args, **kwargs):

        with open('log_function.log', 'a', encoding='utf-8') as log_file:
            log_file.write(f"{datetime.datetime.now().replace(microsecond=0)},"
                            f" name: {some_function.__name__}, arguments: {args} {kwargs},"
                            f" result: {some_function(*args, **kwargs)}\n")

        return some_function(*args, **kwargs)
    return write_fun


 #Пораметризованный Декоратор для задния №2
def logger2(path):
    def logger(some_function):

        def write_fun(*args, **kwargs):

            with open(path, 'a', encoding='utf-8') as log_file:
                log_file.write(f"{datetime.datetime.now().replace(microsecond=0)}, "
                               f"name: {some_function.__name__}, arguments: {args} {kwargs},"
                               f" result: {some_function(*args, **kwargs)}\n")

            return some_function(*args, **kwargs)
        return write_fun
    return logger

