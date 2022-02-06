import random

print("Hi this is a game of guessing the number which I have in my mind")
print("choose difficulty: E (easy), M (medium), H (hard)")
cd=input(": ")
print("I have choosen the number, guess it!!")

if (cd.upper()=='E'):
    num=random.randint(0,15)
elif (cd.upper()=='M'):
    num=random.randint(0,50)
else:
    num=random.randint(0,100)

while (True):
    ui=int(input("guess the number: \n"))
    if(ui==num):
        print("Brilliant!! you made it!!! ")
        print(f"The number was {num}")
        i= input("do you want to play again? (y/n): ")
        if (i.lower()=="y"):
            print("choose difficulty: E (easy), M (medium), H (hard)")
            cd = input(": ")
            if (cd.upper() == 'E'):
                num = random.randint(0, 15)
            elif (cd.upper() == 'M'):
                num = random.randint(0, 50)
            else:
                num = random.randint(0, 100)
            continue
        else:
           quit("thanks for playing!!!")
    elif (num>ui):
        print("my number is greater!!")
    else:
        print("my number is smaller")