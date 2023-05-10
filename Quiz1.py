import time

print('''
######################################
####        GOODNESS' QUIZ        ##########################
######################################
              ################
     ###################
 ##############           ################
#########################
                 ##################
                 #####################################
''')
record = {}
res = 'y'
while res.lower() in ('y', 'yes'):

    print('Enter your name: ')

    name = input('')
    print('Welcome', name.upper() , 'get ready to start')
    score = 0


    print('''
    1. What is the full meaning of HP?
    (a) Helen Margaret
    (b) Hewlett Packard
    (c) Hostile Plenty
    (d) hewlard package
    ''')

    ans = input('Enter a-d')
    if ans.lower() == 'b':
        print('Correct Answer!')
        score += 1
    else:
        print('Wrong Answer!')
        print('The correct answer is b')

    print('''
    2. Who is the president of Russia?
    (a) Dr. Helen Paul
    (b) Sir Herbert Macauly
    (c) Vladimir Putin
    (d) Titilayo Buhari
    ''')

    ans = input('Enter a-d')
    if ans.lower() == 'c':
        print('Correct Answer!')
        score += 1
    else:
        print('Wrong Answer!')
        print('The correct answer is c')

    print('''
    3. What is the largest mammal on Earth?
    (a) Blue Whale
    (b) Elephant
    (c) Girraffe
    (d) Gorrilla
    ''')

    ans = input('Enter a-d')
    if ans.lower() == 'a':
        print('Correct Answer!')
        score += 1
    else:
        print('Wrong Answer!')
        print('The correct answer is a')

    print('''
    4. What is the capital of the United States of America?
    (a) New Jersey
    (b) New York
    (c) California
    (d) Washington DC
    ''')

    ans = input('Enter a-d')
    if ans.lower() == 'd':
        print('Correct Answer!')
        score += 1
    else:
        print('Wrong Answer!')
        print('The correct answer is d')

    print('''
    5. Which of the following is not a Python data type?
    (a) Number
    (b) Array
    (c) List
    (d) None of the above
    ''')

    ans = input('Enter a-d')
    if ans.lower() == 'b':
        print('Correct Answer!')
        score += 1
    else:
        print('Wrong Answer!')
        print('The correct answer is b')

    record.update({name: str(score*20) + '%'})

    print('Do you want to try again? (y/n)')
    res = input("")

print('You have come to the end of the quiz, \
your result will be posted shortly')

dot = ''
for i in range(1,6):
    dot += "."
    print('Please Wait', dot)
    time.sleep(1)
print(record)