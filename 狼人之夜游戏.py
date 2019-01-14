import time
#引用时间模块。
superdict = {}
#定义了一个字典，字典里的内容是页码对应故事。此处省略。
print('''古代欧洲，爆发瘟疫，人们纷纷死去，一个叫做亚历山大·柯文纳斯的军头也感染了疾病，但只有他一个人活了下来。亚历山大的孩子一共有3位，不幸的是其中两位－马库斯与威廉，一个被蝙蝠咬伤，另一个却狼咬伤，只有一位作为普通人。两个兄弟由于病毒产生变异，一位成为吸血鬼的始祖，另一位成为狼人的始祖。从此狼人和吸血鬼便在欧洲流传开来……
许多年以后……''')
#就是最简单的print。
time.sleep(3)
#程序休息3秒，再运行。
num=input('''
回复1开始《狼人之夜》游戏。
>''')
#启动游戏。
goodend = [74,77,22,49]
#这些页码，是好的结局。
badend = [52,75,69,33,75,63,62,61,35]
#这些页码，是坏的结局。
game=[]
#创建一个空列表，用来记录用户的选择。
time.sleep(1)
#程序休息1秒。
while True:
#创建一个循环。
      game.append(num)
      #记录用户输入的页码。
      print(superdict['page'+num])
      #打印出用户选择页码，对应的内容。
      time.sleep(3)
      #休息3秒。
      if int(num) in goodend:
      #如果用户输入的页码，是好结局所在页码，那么：
          f = open('D:\\游戏记录.txt','a+')
          #在电脑D盘的根目录下，创建一个txt文档。
          for x in game:
          #遍历游戏记录。
              f.write(superdict['page'+str(x)]+'\n\n')
              #写入故事。
              f.close
              #关闭文档。
          input('''luck Dog!
恭喜你，成功通关本游戏。
游戏记录已保存至D盘根目录下！
点击Enter即可退出游戏~
注：游戏脚本出自《狼人之夜》。
原作者为汤姆·B·斯通（Tom B. Stone）。
>''')
          break
          #结束循环
      if int(num) in badend:
      #类比，好结局那部分的代码。
          f = open('D:\\游戏记录.txt','a+')
          for x in game:
              f.write(superdict['page'+str(x)]+'\n\n')
              f.close
          input('''Bad Ending!
恭喜你，成功通关本游戏。
游戏记录已保存至D盘根目录下！
点击Enter即可退出游戏~
注：游戏脚本出自《狼人之夜》。
原作者为汤姆·B·斯通（Tom B. Stone）。
>''')
          break
          #跳出循环。
      num = input('请输入数字编码：')
      #如果没触发结局，让用户继续输入页码。