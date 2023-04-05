import pandas as pd
import numpy as np


chat_id = 1112920502 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    a = (np.log(11-x.mean())-1)
    return a
    
