#请使用while循环打印99乘法表
# 1*1=1
# 1*2=2 2*2=4
# 1*3=3 2*3=6 3*3=9
a=0
b=0
while a<9:
    a=a+1
    while b<9:
        b=b+1
        print(b,"*",a,"=",a*b,"\t",end="")
        if a==b:
            b=0
            print("")
            break
print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x*y)
                           for y in range(1, x+1)]) for x in range(1, 10)]))
