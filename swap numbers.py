def swap_numbers():
    print('Enter first number here')
    num1 = input('>>>')
    print('Enter second number here')
    num2 = input('>>>')
    print'Your first number is' ,num1
    time.sleep(4)
    print'Your second number is' ,num2
    time.sleep(4)
    change = num1
    num1 = num2
    num2 = change
    print'I will change your values magically in 5,',
    time.sleep(1)
    print'4,',
    time.sleep(1)
    print'3,',
    time.sleep(1)
    print'2,',
    time.sleep(1)
    print'1'
    print 'abracadabra'
    time.sleep(3)
    print 'and some other magic words, i don\'t know'
    time.sleep(3)
    print 'Now'
    print 'Your first number is',num1
    print 'Second number is',num2
    return
import time
swap_numbers()
