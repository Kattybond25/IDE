"""Игра угадай число за 20 попыток"""
import numpy as np
import random as rd

def guess_number(target_number):
    low_limit=1 #нижний предел диапазона чисел
    up_limit=100 #верхний предел диапазона чисел
    attempts=0 # счетчик попыток
    while True:
        guessed_number=(low_limit+up_limit)//2 # Вычисляем середину диапазона
        attempts+=1 # увеличиваем счетчик попыток на 1
        if guessed_number==target_number:
            return attempts # если предполагаемое число совпадает с целевым, возвращаем количество попыток
        elif guessed_number<target_number:
            low_limit=guessed_number+1 # корректируем нижний предел для следующей итерации
        else:
            up_limit=guessed_number-1 # корректируем верхний предел для следующей итерации
target_number=rd.randint(1,100) # генерируем случайное число от 1 до 100
attempts_needed=guess_number(target_number)
print(f"{target_number} was found for {attempts_needed} attempts")
def score_game(guess_function):
    # устанавливаем количество раундов для проверки
    number_of_rounds = 1000
    total_attempts = 0
    
    for _ in range(number_of_rounds): # генерируем случайное число для каждого раунда
        target_number = rd.randint(1, 100)
        
        # вызываем функцию угадывания числа и суммируем попытки
        attempts = guess_function(target_number)
        total_attempts += attempts
    
    average_attempts = total_attempts / number_of_rounds # среднее количество попыток для угадывания
    print(f"Average number of attempts to guess: {average_attempts}")

# Вызываем функцию для оценки игры
score_game(guess_number)





# угадываем число и выводим количество попыток
    