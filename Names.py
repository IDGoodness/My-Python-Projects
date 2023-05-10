print("WELCOME TO WORD QUIZZ ")
print("LET GET STARTED ")
print("ENTER ALL INPUTS IN UPPER CASE ")
name = input("Enter your name: ")
age = float(input("Enter your age: " ))
if age >= 18 :
    gender = input("Enter your gender(M/F): ")
    aa = input("Are you a (MISS/MRS): ")
    if gender.lower()  == "m" :
        print(f"Your are welcome Mr. {name} ")
    elif gender.lower() == "f" :
        if aa.lower() == "miss":
            print(f"Your are welcome Miss. {name} ")
        elif aa.lower() == "mrs":
            print(f"Your are welcome Mrs. {name} ")
        else:
            print("INVALID INPUT !!!")
    else:
        print("INVALID INPUT !!!")
else:
    print("Come back when you are 18")
print("BABIES IN THEIR FIRST THREE MONTHS LOVE")
print("A - Football")
print("B - Bowling")
print("C - Sleeping")
print("D - Jumping")
que1 = input("Enter your answer (A/B/C/D) ")
score = 0
if que1.lower() =="c":
    score += 1

print("THE FIRST AFRICAN TO WIN BALON D'OR IS? ")
print("A - Mikel Obi")
print("B - Mohammed Salah")
print("C - Samuel Etoo")
print("D - George Weah")
que2 = input("Enter your answer (A/B/C/D) ")
if que2.lower() =="D" :
    score += 1

print("The founder of Microsoft Corporation is? ")
print("A - Jeff Bezos")
print("B - Warren Buffet")
print("C - Blaise Pascal")
print("D - Bill Gate")
que3 = input("Enter your answer (A/B/C/D) ")
if que3.lower() =="d" =='D' :
    score += 1

if gender.lower() == "m" :
    print(f"You scored {score} Mr. {name} ")
if aa.lower() == "miss":
    print(f"You scored {score} Miss. {name} ")
if aa.lower() == "mrs":
    print(f"Your scored {score} Mrs. {name} ")

print("THANKS FOR PLAYING")