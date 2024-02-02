import random
from multiprocessing import Pool
import os

MILLION = 1_000_000
PROCESSES = 20

ATTEMPTS = 12
NUMBER_TO_ROLL = 6

def dice_roll(_):
    succ = 0
    for _ in range(MILLION):
        for _ in range(ATTEMPTS):  # 12 attempts
            if random.randint(1, 6) == NUMBER_TO_ROLL:   # rolling a 6 given a fair 6 sided die
                    succ += 1
                    break
    return succ

if __name__ == '__main__':
    pool = Pool()
    results = pool.map(dice_roll, range(PROCESSES))  # Pass a range as an iterable
    print(results)
    print(sum(results)/ ((PROCESSES)*MILLION))
    