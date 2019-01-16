#使用gbk 来编码自己的名字
print('孙乾坤'.encode('gbk'))
#使用utf-8 来编码自己的名字
print('孙乾坤'.encode('utf-8'))


print(ord('孙'))
#得到的结果会是23385，这是用十进制表示的数。
print(chr(23385))
#chr()的用法和ord()的用法是恰好相反的，可以把整数编码，变成汉字。

print(b'\xb7\xe7\xb1\xe4\xbf\xc6\xbc\xbc\xd3\xd0\xd2\xe2\xcb\xbc'.decode('gbk'))
#使用gbk解码b'\xb7\xe7\xb1\xe4\xbf\xc6\xbc\xbc\xd3\xd0\xd2\xe2\xcb\xbc'