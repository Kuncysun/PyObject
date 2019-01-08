'''for循环语法结构：
for iterating_var in sequence:
   statements(s)'''
   
sunNum=0
for a in range(1,101):#range(start,stop)函数  一般和for循环一起使用 表示 开始位置到结尾位置之间的值   range(1,101)表示1-100 左闭右开（左包含右不包含）
    # for in 
    # sunNum+=a   等价于 sunNum=sunNum+a   同理：sunNum-=a 等价于 sunNum=sunNum-a  还有*=  /=  不常用最后两种
    sunNum+=a
print(sunNum)  






#说了这么多，那这计算求和算不算一个单独的功能了？是的话一般我们 写程序经常把这个 功能 包装加工起来 作为一个方法来使用
#这个方法我们称之为函数

#函数的定义：def fun(参数)：
#               要做什么  这题是要做1+2+3+4+5.....+100 的和
#               return 返回值
#那把上面的代码封装成一个函数怎么写呢？看如下代码

def funNum():
    sunNum=0
    for a in range(1,101):
        sunNum+=a
    return(print(sunNum))   #函数的返回值 


funNum()  #函数的调用  

   








    