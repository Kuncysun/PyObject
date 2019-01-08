import sys

a = 0
while True:
    a = a + 1
    if a == 2:
        try:
          exit()
        except:
            print('Sorry,system is exit!')
        
print(a)
