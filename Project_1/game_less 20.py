"""Игра угадай число за 20 попыток"""
import numpy as np
import random as rd
rd.seed()
number = np.random.randint(1, 100) # загадываем число
# количество попыток
count=0
low_limit=1
high_limit=100
number = rd.randint(low_limit, high_limit)
while True and count<20:
    predict_number = int(input("Угадай число от 1 до 100"))
    count+=1
    if predict_number <1 or predict_number>100:
        print(" Число вне диапазона")
        break
    if predict_number==number:
        print(f"угадано число {number} за {count} попыток.")
        break
    elif predict_number<number:
        print ( f'Попытка {count}, ваше число меньше меньше задуманного на {number-predict_number}')
    else:
        print (f'Попытка {count}, ваше число больше задуманного на {predict_number-number}')