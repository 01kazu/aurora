def randomNumbers():
    print('How many numbers do you want to generate?')
    num=input('>>>>')
    for random_num in range(0,num+1):
        digit = random.randint(1,100)
        print digit,'\t',
    return
import random
import time
start_time = time.clock()
randomNumbers()
print '\n',time.clock()-start_time,'seconds'
