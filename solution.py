import pandas as pd
import numpy as np


chat_id = 1112920502 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    mu = -1-np.exp(1) # математическое ожидание ошибок измерения
    var = (np.exp(2)-2)*mu**2 # дисперсия ошибок измерения
    a = 10/(x.mean()**2) # оценка коэффициента ускорения по методу моментов
    return a # Ваш ответ
    
