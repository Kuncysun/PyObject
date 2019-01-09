#模仿一下内置函数 abs() 定义我们自己的函数 my_abs()  
# 对参数类型做检查，只允许整数和浮点数类型的参数。
# 数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
a=my_abs(-9)
print(a)
#my_abs('A')
        