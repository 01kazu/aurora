import random
def guessGame():
    number = random.randint(1, 100)
    trials = 0
    guess = 0
    while (guess != number):
        if (trials == 5):
           print(" SORRY, YOU'VE LOST ALL YOUR CHANCES")
           print(" THE CORRECT NUMBER IS " + str(number))
           break
        print(" what is the number ?")
        guess=input(" >> ")
        trials+=1
        if (guess > number):
            print(" YOUR GUESS IS BIGGER THAN THE NUMBER ")
        if (guess < number): 
            print(" YOUR GUESS IS SMALLER THAN THE NUMBER ")
        if(guess > 100):
            print(" YOUR GUESS IS BIGGER THAN 100 ")
    if (guess == number):
            print("CONGRATULATIONS, YOU GOT THE NUMBER")
def playAgain():
    print(" HELLO, WHAT'S YOUR NAME ? ")
    name = raw_input(" >> ")
    print( 'HELLO '+name.upper()+', YOU\'RE ABOUT TO PLAY A GUESS GAME')
    print("YOU ARE TO GUESS A NUMBER FROM 1 TO 100 AND YOU HAVE FIVE TRIES, GOOD LUCK!!!!")
    answer = 0
    while( answer != 'n'):
       print(" DO YOU WANNA PLAY  ")
       print("Y or N")
       answer = raw_input(' >> ')
       if (answer == "Y" or answer == 'y'): 
            guessGame()
       elif (answer == "N" or answer == 'n'):
            print(' THANKS FOR PLAYING, GOODBYE!!!!')
            break
       else:
           print('PLEASE TYPE \'Y\' TO PLAY OR \'N\' TO NOT PLAY ')
import time
start_time = time.clock()
playAgain()
print "this program lasted for "+str(time.clock()-start_time),"seconds"
