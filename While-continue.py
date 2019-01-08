while True:
    q1 = input('第一问：你一生之中，在什么地方最是快乐逍遥？')
    if q1 != '黑暗的冰窖':
        continue
    print('答对了，下面是第二问：')
    q2 = input('你生平最爱之人，叫什么名字？')
    if q2 != '梦姑':
        continue
    print('答对了，下面是第三问：')
    q3 = input('你最爱的这个人相貌如何？')
    if q3 == '不知道':
        break
print('都答对了，你是虚竹。')
