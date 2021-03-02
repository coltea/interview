

#
# def func_log(func):
#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         print(f"t1:{t1}")
#         func(*args, **kwargs)
#         print(f'函数入参: *args:{args}, **kwargs: {kwargs} ')
#         print(f"总运行时间:{round(time.time() - t1, 4)}")
#
#     return wrapper

import time


def log_time_de(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        func(*args, **kwargs)
        print(f"运行时间:{time.time()-t0}")
    return wrapper


@log_time_de
def log_time(a=12, b=12122):
    print("run")
    time.sleep(2)
#
#
# def get(function):
#     def wrapper(*arg, **kwargs):
#         return function(*arg, **kwargs)
#
#     return wrapper
#
#
# def check_para(para_type):
#     def decorate(func):
#         def wrapper(*args, **kwargs):
#             for i in args:
#                 if isinstance(i, para_type):
#                     print("suucess", i)
#                 else:
#                     print("error", i)
#             func(*args, **kwargs)
#
#         return wrapper
#
#     return decorate
#
#
# @check_para(int)
# def get_data(*args):
#     for i in args:
#         print(i)


if __name__ == '__main__':
    # get_data(1, "ksye", 3)

    log_time(12, 12122)
