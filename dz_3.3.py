def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg3 > arg1 > arg2:
        return arg1 + arg3
    else:
        return arg2 + arg3
print(my_func (5, 6, 1))