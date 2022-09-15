"""Guess the number game
The computer riddles and guesses the number 
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """guess the number randomly

    Args:
        number (int, optional): The number which the computer has in mind. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    count = 0
    number = np.random.randint(1, 101) # computer chooses the number
    max1 = 101
    min1 = 1
    

    while True:
        count += 1
        mid1 = round((max1 + min1)/2)
           
        if number == mid1:
            break  # Exit the cycle if the number is guessed
        
        if number > mid1:
            min1 = mid1
            
        if number < mid1:
            max1 = mid1
        
        if count > 20: break
      
    return count




def score_game(random_predict) -> int:
    """How many tries does our algorithm use in an average of 1000 tries?

    Args:
        random_predict ([type]): guessing function

    Returns:
        int: average number of attempts
    """
    count_ls = []
    #np.random.seed(1)  # fix the seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000))  # riddled with a list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number in an average of :{score} attempts")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
