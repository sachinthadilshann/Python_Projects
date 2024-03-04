from random import randint

lower_num , higest_num = 1,10

random_num: int = randint(lower_num,higest_num)
print(f'Guss the number in the range from {lower_num}  to {higest_num}')

while True:

    try:
        user_guess: int = int(input("Guess: "))
    except ValueError as e:
        print("Plz Enter Valid Number!!!!")
        continue

    if user_guess > random_num:
        print("The Number is Low: ")
    elif user_guess < random_num:
        print("The Number is higer")
    else:
        print("You guessed it")
        break