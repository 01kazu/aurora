def files_count_vowels():
    print 'Please write the name of your file'
    file_name = raw_input('>>>')
    open_file = open(file_name + '.txt','r')
    read_file = open_file.read().lower()
    vowels = 'aeiou'
    count_v = 0
    for letter in read_file:
        if letter in vowels:
            count_v += 1
    print 'The number of vowels in your text file (%s) is %d' %(file_name,count_v)
    return
def files_count_consonants():
    print 'Please write the name of your file'
    open_file = open(file_name + '.txt','r')
    read_file = open_file.read().lower()
    consonants = 'bcdfghjklmnpqrstvwxyz'
    count_c = 0
    for letter in read_file:
        if letter in consonants:
            count_c += 1
    print 'The number of consonants in your text file (%s) is %d' % (file_name, count_c)
    open_file.close()
    return
def files_count_alphabets():
    print 'Please write the name of your file'
    file_name = raw_input('>>>')
    open_file = open(file_name + '.txt', 'r')
    read_file = open_file.read().lower()
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    count_a = 0
    for letter in read_file:
        if letter in alphabets:
            count_a += 1
    print 'The number of alphabets in your text file (%s) is %d' % (file_name, count_a)
def write_files():
    print 'Enter the name of the new file you wish to create '
    file_new_name = raw_input('>>>')
    write_file = open(file_new_name+".txt",'w')
    print'Write contents of file below'
    contents = raw_input('>>>')
    write_file.write(contents)
    write_file.close()
    return
def view_files():
    print'Enter the name of the file you wish to view below'
    file_name = raw_input('>>>')
    open_file = open(file_name+".txt",'r')
    open_file.read()
    open_file.close()
    return
def add_to_files():
    print'Enter the name of the file you wish to add contents below'

    file_name = raw_input('>>>')
    open_file = open(file_name + ".txt", 'a')
    pass
end = True
while end == True:
         print'1 = Do you want to create a new file ?'
         print'2 = Do you want to view the contents of your file?'
         print'3 = Do you want count vowels and consonants in your file ?'
         print('Type the number of the option below')
         choice = input('>>>')
         if (choice == 1):
             write_files()
         if (choice == 2):
             view_files()
         if (choice == 3):
             print 'If you want to know the number of consonants, type c'
             print 'If you want to know the number of vowels, type v'
             print 'If you want to know the number of alphabets,type a'
             choice_letters = raw_input('>>>').lower()
             if (choice_letters == 'c'):
                 files_count_consonants()
             if (choice_letters == 'v'):
                 files_count_vowels()
             if (choice_letters == 'a'):
                 files_count_alphabets()
             else:
                print'Invalid choice'
                print' Please pick from the listed options A,C or V'
         while end == True:     
             print "If done, type 'y' for yes else type 'n' for no" 
             end = raw_input('>>>').lower()
             if end == 'y':
                   end.isdigit()
             elif end == 'n':
                 end = True
                 break
             else:
                print 'Invalid input'
                print "If done, type 'y' for yes else type 'n' for no"
                end = True
print'Thank you for using my text file program'
        
             
         
        




    
