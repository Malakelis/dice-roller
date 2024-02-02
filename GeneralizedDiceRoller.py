import random
from multiprocessing import Pool
import os

MILLION = 10_000_000
PROCESSES = 20




def dice_roll(NUMBER_TO_ROLL, HOW_MANY, ATTEMPTS):
    succ = 0
    for _ in range(MILLION):
        check = 0
        for _ in range(ATTEMPTS):  # 12 attempts
            if random.randint(1, 6) == NUMBER_TO_ROLL:   # rolling a 6 given a fair 6 sided die
                check += 1
                if check == HOW_MANY:   # rolling 2 6s
                    succ += 1
                    break
    return succ

if __name__ == '__main__':
    NUMBER_TO_ROLL = int(input("What do you want to roll? "))
    HOW_MANY = int(input("How many successes? "))
    ATTEMPTS = int(input("How many attempts? "))

    pool = Pool()
    args = [(NUMBER_TO_ROLL, HOW_MANY, ATTEMPTS)] * PROCESSES
    results = pool.starmap(dice_roll, args)  # starmap instead of map for multiple arguments
    print(results)
    print(sum(results)/ ((PROCESSES)*MILLION))
    