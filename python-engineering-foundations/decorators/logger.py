# def logger(func):
#     def wrapper(*args,**kwargs):#reference to the original function
#         print(f"Start {func.__name__} function")
#         print(f"Arguments: {args} {kwargs}")
#         result=func(*args,**kwargs) #acts as add function
#         print(f"End {func.__name__} function")
#         return result
#     return wrapper
# #decorator
# @logger
# def add(a,b):
#     # print(a+b)
#     return a+b

# # @logger
# # def mutiply(a,b):
# #     print(a*b)
# #     return a*b

# print(f"Result: {add(10,30)}")
# # print(f"Result: {mutiply(10,30)}")


def outer():
    x=10
    def inner():
        return x
    return inner

f=outer()
print(f.__closure__) #closure object
print(f.__closure__[0].cell_contents) #value of x in closure