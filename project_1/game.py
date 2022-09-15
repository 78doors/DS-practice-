"""Guess the number"""

import numpy as np

number = np.random.randint(1, 101) # computer chooses the number

# number of attempts
count = 0

while True:
    count+=1
    predict_number = int(input("Guess the number from 1 to 100: "))
    
    if predict_number > number:
        print("The number must be less!")

    elif predict_number < number:
        print("The number must be greater!")
    
    else:
        print(f"You guessed the number! This number is  {number}, and you've used {count} attempts")
        break #game is over, quitting.
