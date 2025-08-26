print("Lesson 7. Home task №4.")
"""
4. Сделать декоратор, который измеряет время, затраченное
на выполнение декорируемой функции
"""


import time

def function_execution_time(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        execution_time = end - start
        print(f'Время выполнения функции: {execution_time}')
        return result
    return wrapper


@function_execution_time
def fast_function():
    time.sleep(2)
    print("Быстрая функция завершила работу!")


@function_execution_time
def slow_function():
    time.sleep(4)
    print("Медленная функция завершила работу!")

fast_function()
slow_function()
