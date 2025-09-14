import random

target_number = random.randint(1, 100)
while True:
    try:
        guess = int(input('Guess number from 1 and 100: '))
        if guess < target_number:
            print('Too low!')
        elif guess > target_number:
            print('Too high!')
        else:
            print('Congratulations!')
            break
    except ValueError: 
        print('Enter a valid number')

