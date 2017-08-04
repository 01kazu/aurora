def elimination_method():

    return
def explanation_part1():
    print '''LET'S USE AN EXAMPLE FROM YOUR WORK TO GUIDE US ALL THE WAY THROUGH \n
             1 FIND THE VALUE OF X AND Y IN THE SIMUETANEOUS EQUATION BELOW\n
                                %.2fX + %.2fY = %.2f   ------>(1)\n 
                                %.2fX + %.2fY = %.2f  ------>(2)  ''' %(num_X1,num_Y1,num1,num_X2,num_Y2,num2)
    sleep(10)
    print 'LET %.2fX + %.2fY = %.2f BE CALLED EQUATION 1 OR (1)' %(num_X1,num_Y1,num1)
    sleep(3)
    print 'LET %.2fX + %.2fY = %.2f BE CALLED EQUATION 2 OR (2)' %(num_X2,num_Y2,num2)
    sleep(4)
    print 'FIRST THING TO DO IS TO MULTIPLY THE EQUATION 1 WITH THE CO - EFFICIENT OF THE X IN THE EQUATION 2'
    sleep(4)
    print'NOW REMEMBER WE ARE GETTING OUR VALUE FROM THE EXAMPLE 1'
    sleep(4)
    print 'TYPE THE CO - EFFICIENT OF X IN EQUATION 2 BELOW'
    trial = float(input('>>>'))
    if trial == num_X2:
        print 'GOOD JOB, YOU GOT IT '
    if trial == num_X2:
        print 'THAT IS THE CO_EFFICIENT OF THE EQUATION 1'
        sleep(3)
        print 'NICE TRY, THOUGH'
        sleep(2)
        print 'THE CO-EFFICIENT OF X IN THE BOTH EQUATIONS IS %.2f AND %.2f' %(num_X1,num_X2)
        sleep(4)
        print 'IN LAME MAN TERMS, THE NUMBER IN FRONT OF X IS %.2f IN EQUATION 1' %(num_X1)
        sleep(4)
        print '                                      --->%.2f<---X + %.2fY = %.2f' %(num_X1,num_Y1,num1)
        sleep(2)
        print 'AND '
        sleep(1)
        print '3 IN EQUATION 2'
        sleep(2)
        print '                                      --->%.2f<---X + %.2fY = %.2f' %(num_X2,num_Y2,num2)
        sleep(3)
    else:
        print 'SORRY, THAT IS NOT THE CO_EFFICIENT OF X '
        sleep(3)
        print 'THE CO-EFFICIENT OF X IN THE BOTH EQUATIONS IS %.2f AND %.2f' % (num_X1, num_X2)
        sleep(4)
        print 'IN LAME MAN TERMS, THE NUMBER IN FRONT OF X IS %.2f IN EQUATION 1' % (num_X1)
        sleep(4)
        print '                                      --->%.2f<---X + %.2fY = %.2f' % (num_X1, num_Y1, num1)
        sleep(3)
        print 'AND '
        sleep(1)
        print '%.2f IN EQUATION 2' %(num_X2)
        sleep(3)
        print '                                      --->%.2f<---X + %.2fY = %.2f' % (num_X2, num_Y2, num2)
    return
def explanation_part2():
    print 'NOW THAT WE KNOW THE CO-EFFICIENT OF X IN EQUATION 2 IS %.2f, WHAT ARE WE GONNA DO WITH THAT?' %(num_X2)
    sleep(5)
    print 'I WANT YOU TO FOLLOW ME EVERY STEP I GO,  BECAUSE I WANT YOU TO UNDERSTAND THIS'
    sleep(5)
    print 'WE ARE GOING TO MULTIPLY EACH TERM IN EQUATION 1 WITH THE CO-EFFICIENT OF X IN EQUATION 2 WHICH IS %.2F' %(num_X2)
    sleep(7)
    print 'THEREFORE, IT IS GOING TO BE '
    sleep(4)
    print '     (%.2f * %.2fX) + (%.2f * %.2fY) = %.2f * %.2f' %(num_X2, num_X1,num_X2,num_Y1, num_X2,num1)
    sleep(4)
    print 'WHICH WILL CREATE A NEW EQUATION'
    sleep(3)
    print '      (%.2fX + %.2fY = %.2f)    WE WILL CALL THIS EQUATION 3------->(3)' %(change_num_X1,change_num_Y1,change_num1)
    sleep(4)
    print 'THEREFORE WE HAVE THREE EQUATIONS'
    sleep(3)
    print ' |---->  %.2fX + %.2fY = %.2f AS EQUATION 1 ' %(num_X1,num_Y1,num1)
    sleep(4)
    print ' |       %.2fX + %.2fY = %.2f AS EQUATION 2' %(num_X2,num_Y2,num2)
    sleep(4)
    print ' |                 AND'
    sleep(2)
    print ' |-----> %.2fX + %.2fY = %.2f AS EQUATION 3' %(change_num_X1,change_num_Y1,change_num1)
    sleep(4)
    print 'WHAT ARE THE VALUES OF EQUATION 2 WHEN MULTIPLIED BY %.2f' %(num_X1)
    sleep(5)
    print'AS BEFORE WE WOULD MULTIPLY %.2f WITH EACH VALUE' %(num_X1)
    sleep(5)
    print'I HAVE SOME WORK I WANT YOU TO DO '
    sleep(4)
    print'I WANT YOU TO FIND THAT NEW EQUATION FOR ME, DO YOU WANT TO TRY?(Y/N)'
    sleep(5)
    equation4Trial = raw_input('>>>').lower()
    if equation4Trial == 'y':
        print 'NICE ONE, TYPE THE NEW VALUE OF X AND Y BELOW'
        sleep(4)
        print 'ENTER THE VALUE OF THE CO-EFFICIENT OF X IN THE NEW EQUATION'
        equation4Trial_ansX = float(input('>>>'))
        if (equation4Trial_ansX == change_num_X2):
            print'GOOD WORK, YOU GOT THE RIGHT ANSWER'
        else:
            print'NICE TRY, BUT THE CORRECT VALUE IS %.2f' %(change_num_X2)
            sleep(4)
            print'WHEN YOU MULTIPLY %.2f WITH %.2fX + %.2fY = %.2f WHICH IS EQUATION 2' %(num_X1,num_X2,num_Y2,num2)
            sleep(4)
            print'YOU GET %.2f MULTIPLYING EACH VARIABLE IN EQUATION 2' %(num_X1)
            sleep(4)
            print'SO IT BECOMES (%.2f * %.2fX) + (%.2f * %.2fY) = %.2f * %.2f '%(num_X1, num_X2,num_X1,num_Y2, num_X1,num2)
            sleep(4)
            print'SO YOU GET %.2fX + %.2fY = %.2f ' %(change_num_X2,change_num_Y2,change_num2)
            sleep(4)
            print'AND WHAT IS THE NUMBER ASSOCIATED WITH X ?'
            sleep(3)
            print'ITS %.2f' %(change_num_X2)
            sleep(3)
        print 'WHAT IS THE VALUE OF THE CO-EFFICIENT OF Y IN THE NEW EQUATION'
        equation4Trial_ansY = float(input('>>>'))
        if (equation4Trial_ansY == change_num_Y2):
            print'GOOD WORK, YOU GOT THE RIGHT ANSWER'
        else:
            print'NICE TRY, BUT THE CORRECT VALUE IS %.2f' %(change_num_Y2)
            sleep(4)
            print'WHEN YOU MULTIPLY %.2f WITH %.2fX + %.2fY = %.2f WHICH IS EQUATION 2' %(num_X1,num_X2,num_Y2,num2)
            sleep(5)
            print'YOU GET %.2f MULTIPLYING EACH VARIABLE IN EQUATION 2' %(num_X1)
            sleep(4)
            print'SO IT BECOMES (%.2f * %.2fX) + (%.2f * %.2fY) = %.2f * %.2f '%(num_X1, num_X2,num_X1,num_Y2, num_X1,num2)
            sleep(5)
            print'SO YOU GET %.2fX + %.2fY = %.2f ' %(change_num_X2,change_num_Y2,change_num2)
            sleep(5)
            print'AND WHAT IS THE NUMBER ASSOCIATED WITH Y?'
            sleep(3)
            print'ITS %.2f' %(change_num_Y2)
            sleep(2)
    return
def explanation_part3():
    print 'GREAT, DO YOU WANT TO TAKE A BREAK (Y/N)? '
    reply =raw_input('>>>').lower()
    if reply == 'y':
        print 'I\'LL GIVE YOU THREE MINUTES TO REST'
        sleep(4)
        print 'BETTER BE BACK BEFORE THEN OR ELSE '
        sleep(4)
        print 'YOU',
        sleep(1)
        print 'ARE',
        sleep(1)
        print 'ON',
        sleep(1)
        print 'YOUR',
        sleep(1)
        print 'OWN'
        sleep(20)
        print'OKAY CANT WAIT ANY LONGER WE ARE GOING TO START NOW'
    if reply == 'n':
        print 'COOL, LET\'S CONTINUE'
    else:
        print 'OOOOOKAYYY'
        sleep(4)
        print 'I DO NOT KNOW IF THAT IS YES OR A NO SO I\'LL TAKE THAT AS A YES'
        sleep(4)
    print'LET\'S HAVE A RECAP OF WHAT WE HAVE DONE, SHALL WE?'
    sleep(4)
    print'WHEN GIVEN A SIMUETANEOUS EQUATION, FIRSTLY YOU IDENTIFY THE CO-EFFICIENT OF X IN BOTH EQUATIONS'
    sleep(4)
    print'TO CLEAR THINGS UP'
    sleep(3)
    print'ITS NOT IN EVERY CASE THAT THE TWO VARIABLES WILL BE X AND Y'
    sleep(3)
    print'FOR EXAMPLE'
    sleep(2)
    print'FIND THE VALUE OF A AND B IN THE SIMUETANEOUS EQUATION BELOW'
    sleep(4)
    print'''                    %.2fA + %.2fB = %.2f
                                %.2fA + %.2fB = %.2f
                                    or 
          FIND THE VALUE OF D AND P IN THE SIMUETANEOUS EQUATION BELOW
                                %.2fD + %.2fP = %.2f
                                %.2f + %.2fP = %.2f ''' %(num_X1,num_Y1,num1,num_X2,num_Y2,num2,num_X1,num_Y1,num1,num_X2,num_Y2,num2)
    sleep(10)
    print'IN THE END THE IDEA IS TO FIND THE CO-EFFICIENT OF BOTH LETTERS IN THE EQUATIONS ,'
    sleep(4)
    print'AS SHOWN ABOVE  '
    sleep(3)
    print'USE THE VARIABLE IN THE FIRST EQUATION TO MULTIPLY THE SECOND EQUATION'
    sleep(4)
    print'AND USE THE VARIABLE IN THE SECOND EQUATION TO MYLTIPLY THE FIRST EQUATION'
    sleep(4)
    print'LETS MOVE ON'
    sleep(2)
    print'WE HAVE GOTTEN OUR NEW EQUATIONS AFTER MULTIPLYING WHICH IS'
    sleep(4)
    print'          %.2fX + %.2fY =  %.2f ------>(3)' %(change_num_X1,change_num_Y1,change_num1)
    sleep(4)
    print'          %.2fX + %.2fY = %.2f ------>(4)' %(change_num_X2,change_num_Y2,change_num2)
    sleep(4)
    print'NOW WE ARE GOING TO SUBTRACT THE EQUATION IN SUCH A WAY THAT IT BECOMES'
    sleep(4)
    print'          %.2fX + %.2fY =  %.2f'  %(change_num_X1,change_num_Y1,change_num1)
    sleep(2)
    print'       -  %.2fX + %.2fY = %.2f' %(change_num_X2,change_num_Y2,change_num2)
    sleep(2)
    print'       ------------------'
    sleep(1)
    print'   =       %.2f - %.2fY = %.2f' %(change_num_X1-change_num_X2,change_num_Y1-change_num_Y2,change_num1-change_num2)

    print'DO YOU UNDERSTAND WHAT JUST HAPPENED ? (Y/N)'
    understand_ans= raw_input('>>>').lower()
    if understand_ans == 'y':
        print"THAT'S COOL "
        sleep(2)
        print'MAKES WORK EASIER FOR ME'
        sleep(3)
    if understand_ans == 'n':
        print'OKAY, HERE\'S WHAT HAPPENED '
        sleep(4)
        print'I SUBTRACTED EQUATION (4) FROM EQUATION (3)'
        sleep(3)
        print'SO %.2fX - %.2fX = %.2f' %(change_num_X1,change_num_X2,change_num_X1-change_num_X2)
        sleep(3)
        print'   %.2fY - %.2fY = %.2fY' %(change_num_Y1,change_num_Y2,change_num_Y1-change_num_Y2)
        sleep(3)
        print'   %.2f - %.2f  = %.2f' %(change_num1,change_num2,change_num1-change_num2)
        sleep(3)
    else:
        print'STILL DONT KNOW IF THAT IS YES OR NO'
        sleep(3)
        print'SO HOW ABOUT WE AGREE TO CHOOSE Y'
        sleep(3)
    print'NOW    %.2fY = %.2f   ' %(change_num_Y1-change_num_Y2,change_num1-change_num2)
    sleep(2)
    print'WE WOULD NOW DIVIDE BOTH SIDES BY THE CO-EFFICIENT OF Y'
    sleep(4)
    print'CAN YOU TELL ME WHAT THE CO-EFFICIENT IS ?'
    trial = float(input('>>>'))
    if trial == change_num_Y1-change_num_Y2:
        print'EXCELLENT!!!!!!!!'
        sleep(1)
        print'SEND ME YOUR ACCOUNT DETAILS AFTER I\'M DONE'
        sleep(3)
    if trial == -(change_num_Y1-change_num_Y2):
        print'CLOSE BUT THAT\S NOT IT '
        sleep(2)
        print'IN MATHS, SIGNS ARE VERY IMPORTANT'
        sleep(3)
        print'SO THE ANSWER WOULD BE "%.2f" NOT "%.2f"' %(change_num_Y1-change_num_Y2,-(change_num_Y1-change_num_Y2))
        sleep(4)
    else:
        print'SORRY THAT\'S NOT IT'
        sleep(3)
        print'I WANT YOU TO FIGURE IT OUT '
        sleep(3)
        print'LEMME GIVE YOU A HINT'
        sleep(3)
        print'ITS THE NUMBER BESIDE Y'
        sleep(3)
        print'SO WHAT IS IT ?'
        trial_1 = float(input('>>>'))
        if trial_1 == (change_num_Y1-change_num_Y2):
            print'CORRECT YOU GOT IT'
        else:
            print'THAT\'S INCORRECT'
            sleep(2)
            print'THE ANSWER IS %.2f' %(change_num_Y1-change_num_Y2)
            sleep(3)
    return
def explanation_part4():
    print'NOW WE DIVIDE BOTH SIDES BY %.2f, SO WE HAVE' %(change_num_Y1-change_num_Y2)
    sleep(4)
    print'    %.2fY  =   %.2f    ' %(change_num_Y1-change_num_Y2,change_num1-change_num2)
    sleep(2)
    print'    -----      -----'
    sleep(1)
    print'    %.2f       %.2f' %(change_num_Y1-change_num_Y2,change_num_Y1-change_num_Y2)
    sleep(2)
    print'SO WHEN WE DO THAT Y = %.2f' %((change_num2 - change_num1) / (change_num_Y2 - change_num_Y1))
    sleep(3)
    print'SO NOW WE KNOW Y = %.2f, WHAT IS X ?' %((change_num2 - change_num1) / (change_num_Y2 - change_num_Y1))
    sleep(3)
    print'FIRSTLY PICK ANY OF THE FORMULA FROM THE PAST'
    sleep(4)
    print'          %.2fX + %.2fY = %.2f   ------>(1)' %(num_X1,num_Y1,num1)
    sleep(2)
    print'          %.2fX + %.2fY = %.2f   ------>(2)' %(num_X2,num_Y2,num2)
    sleep(2)
    print'          %.2fX + %.2fY = %.2f   ------>(3)' %(change_num_X1,change_num_Y1,change_num1)
    sleep(2)
    print'          %.2fX + %.2fY = %.2f   ------>(4)' %(change_num_X2,change_num_Y2,change_num2)
    sleep(2)

    print'IF YOU WANT TO PICK AN EQUATION YOURSELF TYPE(Y)'
    sleep(3)
    print'IF NOT TYPE (N) AND ILL PICK ONE FOR US TO USE'
    answer = raw_input('>>>').lower()
    list_of_equations = [str(num_X1) + 'X + ' + str(num_Y1) + 'Y = ' + str(num1),
                         str(num_X2) + 'X + ' + str(num_Y2) + 'Y = ' + str(num2),
                         str(change_num_X1) + 'X + ' + str(change_num_Y1) + 'Y = ' + str(change_num1),
                         str(change_num_X2) + 'X + ' + str(change_num_Y2) + 'Y = ' + str(change_num2)]
    if answer == 'y':
        print'ENTER THE NUMBER OF THE EQUATION YOU WANT TO USE ?'
        number = input('>>>')
        number -= 1
        equation = 'YOU HAVE CHOSEN '+list_of_equations[number]
        print equation
    elif answer == 'n':
        print'OKAY ,I\'LL CHOOSE THE EQUATION FOR YOU'
        number = randint(0,3)
        sleep(3)
        equation = 'I HAVE CHOSEN '+ list_of_equations[number]
        print equation
    else:
        print 'STILL DON\'T KNOW WHAT THAT IS SO I\'LL CHOOSE FOR YOU'
        number = randint(0, 3)
        sleep(3)
        equation ='I HAVE CHOSEN ' + list_of_equations[number]
        print equation
    if str(num_X1) in equation:
        print 'SUBSTITUTE Y INTO THE EQUATION AND SOLVE'
        sleep(4)
        print '%.2fX + %.2f *(%.2f) = %.2f' %(num_X1,num_Y1,Y,num1)
        sleep(4)
        print '%.2fX + %.2f = %.2f' %(num_X1, num_Y1 * Y,num1)
        sleep(3)
        print 'COLLECT LIKE TERMS'
        sleep(3)
        print '%.2fX = %.2f - %.2f' %(num_X1, num1,num_Y1 * Y )
        sleep(5)
        print '%.2fX = %.2f' %(num_X1, num1-(num_Y1 * Y))
        sleep(5)
        print 'NOW WE DIVIDE BOTH SIDES BY THE CO-EFFICIENT OF X WHICH IS IN THIS CASE IS %.2f' %(num_X1)
        sleep(4)
        print '%.2fX = %.2f' %(num_X1, num1-(num_Y1 * Y))
        sleep(1)
        print '-----  ------'
        sleep(1)
        print '%.2f    %.2f'  %(num_X1,num_X1)
        sleep(4)
        print 'THEREFORE X = %.2f' %((num1-(num_Y1 * Y))/num_X1)
    if str(num_X2) in equation:
        print 'SUBSTITUTE Y INTO THE EQUATION AND SOLVE'
        sleep(4)
        print '%.2fX + %.2f *(%.2f) = %.2f' % (num_X2, num_Y2, Y, num2)
        sleep(4)
        print '%.2fX + %.2f = %.2f' % (num_X2, num_Y2 * Y, num2)
        sleep(3)
        print 'COLLECT LIKE TERMS'
        sleep(3)
        print '%.2fX = %.2f - %.2f' % (num_X2, num2, num_Y2 * Y)
        sleep(5)
        print '%.2fX = %.2f' % (num_X2, num2 - (num_Y2 * Y))
        sleep(5)
        print 'NOW WE DIVIDE BOTH SIDES BY THE CO-EFFICIENT OF X WHICH IS IN THIS CASE IS %.2f' % (num_X2)
        sleep(4)
        print '%.2fX = %.2f' % (num_X2, num2 - (num_Y2 * Y))
        sleep(1)
        print '-----  ------'
        sleep(1)
        print '%.2f    %.2f' % (num_X2, num_X2)
        sleep(4)
        print 'THEREFORE X = %.2f' % ((num2 - (num_Y2 * Y)) / num_X2)
    if str(change_num_X1) in equation:
        print 'SUBSTITUTE Y INTO THE EQUATION AND SOLVE'
        sleep(4)
        print '%.2fX + %.2f *(%.2f) = %.2f' % (change_num_X1, change_num_Y1, Y, change_num1)
        sleep(4)
        print '%.2fX + %.2f = %.2f' % (change_num_X1, change_num_Y1 * Y, change_num1)
        sleep(3)
        print 'COLLECT LIKE TERMS'
        sleep(3)
        print '%.2fX = %.2f - %.2f' % (change_num_X1, change_num1, change_num_Y1 * Y)
        sleep(5)
        print '%.2fX = %.2f' % (change_num_X1, change_num1 - (change_num_Y1 * Y))
        sleep(5)
        print 'NOW WE DIVIDE BOTH SIDES BY THE CO-EFFICIENT OF X WHICH IS IN THIS CASE IS %.2f' % (num_X1)
        sleep(4)
        print '%.2fX = %.2f' % (change_num_X1, change_num1 - (change_num_Y1 * Y))
        sleep(1)
        print '-----  ------'
        sleep(1)
        print '%.2f    %.2f' % (change_num_X1, change_num_X1)
        sleep(4)
        print 'THEREFORE X = %.2f' % ((change_num1 - (change_num_Y1 * Y)) / change_num_X1)
    if str(change_num_X2) in equation:
        print 'SUBSTITUTE Y INTO THE EQUATION AND SOLVE'
        sleep(4)
        print '%.2fX + %.2f *(%.2f) = %.2f' % (change_num_X2, change_num_Y2, Y, change_num2)
        sleep(4)
        print '%.2fX + %.2f = %.2f' % (change_num_X2, change_num_Y2 * Y, change_num2)
        sleep(3)
        print 'COLLECT LIKE TERMS'
        sleep(3)
        print '%.2fX = %.2f - %.2f' % (change_num_X2, change_num2, change_num_Y2 * Y)
        sleep(5)
        print '%.2fX = %.2f' % (change_num_X2, change_num2 - (change_num_Y2 * Y))
        sleep(5)
        print 'NOW WE DIVIDE BOTH SIDES BY THE CO-EFFICIENT OF X WHICH IS IN THIS CASE IS %.2f' % (num_X2)
        sleep(4)
        print '%.2fX = %.2f' % (change_num_X2, change_num2 - (change_num_Y2 * Y))
        sleep(1)
        print '-----  ------'
        sleep(1)
        print '%.2f    %.2f' % (change_num_X2, change_num_X2)
        sleep(4)
        print 'THEREFORE X = %.2f' % ((change_num2 - (change_num_Y2 * Y)) / change_num_X2)
from random import randint
from time import sleep
print "HELLO, WHAT'S YOUR NAME ?"
name = raw_input('>>>').upper()
print "WELCOME", name + ", THIS IS PROGRAM THAT SOLVES SIMUTANUEOUS EQUATIONS"
sleep(3)
print 'YOUR EQUATION SHOULD BE IN THIS FORMAT aX+bY=C'
print '                                       dX+eY=F'
num_X1 = float(input('>>> WHAT IS THE VALUE OF a = '))
num_Y1 = float(input('>>> WHAT IS THE VALUE OF b = '))
num1 = float(input('>>> WHAT IS THE VALUE OF C = '))
num_X2 = float(input('>>> WHAT IS THE VALUE OF d = '))
num_Y2 = float(input('>>> WHAT IS THE VALUE OF e = '))
num2 = float(input('>>> WHAT IS THE VALUE OF F = '))
change_num_X1 = num_X1 * num_X2
change_num_Y1 = num_Y1 * num_X2
change_num1 = num1 * num_X2
change_num_X2 = num_X2 * num_X1
change_num_Y2 = num_Y2 * num_X1
change_num2 = num2 * num_X1
Y = (change_num2 - change_num1) / (change_num_Y2 - change_num_Y1)
X = (change_num1 - (change_num_Y1 * Y)) / change_num_X1
print "THE VALUES OF X and Y IS " + str(X) + ' AND ' + str(Y) + ' respectively'
print'IF YOU WANT TO LEARN HOW TO SOLVE SIMUETANEOUS EQUATIONS TYPE(Y/N)'
choice = raw_input('>>>').lower()
if choice == 'y':
    explanation_part1()
    explanation_part2()
    explanation_part3()
    explanation_part4()
    print 'THANK YOU FOR USING MY PROGRAM MR/MRS/MISS %s' %(name)
elif choice == 'n':
    print'THATS COOL THANKS FOR USING MY PROGRAM THOUGH MR/MRS/MISS %s GOODBYE' %(name)
else:
    print'DONT KNOW IF THAT IS YES OR A NO'
    sleep(3)
    print'SO ILL END THE PROGRAM'
    sleep(3)
    print'HOPE YOU\'LL USE MY PROGRAM AGAIN, MR/MRS/MISS %s' %(name)

