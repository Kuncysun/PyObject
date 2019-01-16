def love(words):
    import time
    for i in words.split():
        print('\n'.join([''.join([(i[(x-y) % len(i)] 
        if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 
        else ' ') 
        for x in range(-30, 30)]) for y in range(12, -12, -1)]))
        time.sleep(1.5)

love('x')

