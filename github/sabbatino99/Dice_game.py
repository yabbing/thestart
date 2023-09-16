import random

dice = [1,2,3,4,5,6]
roll_again = 'yes'

while roll_again == 'yes' or roll_again == 'y':

    value1 = random.choice(dice)
    value2 = random.choice(dice)
    print(value1, value2)
    

    roll_again = input('Press Y or yes to roll dices again.')
    pass