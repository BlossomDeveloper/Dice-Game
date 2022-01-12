import random

# define user and dice numbers

user_number = int(input('Please enter a number between 1 and 6: '))

dice_number = int(random.randint(1, 6))

while 1 < user_number <= 6:
    if user_number >= 1 <= 6:
        print('Your choice: ', int(user_number))
        break
else:
    print(input('Please enter a number between 1 and 6: '))

# Program prompts user for a 2nd number and do the sum to see who will win

user_number2 = int(input('Please enter a number again:'))

num_sum = user_number + user_number2
print('Dice choice: ', int(dice_number))

if dice_number > num_sum:
    print('Sorry the dice won! Try again if you dare to win the dice!')
elif dice_number == num_sum:
    print("It's a tie! Try again to see if you can beat the dice :)")
else:
    print("Congratulations! You've beaten the dice!")




