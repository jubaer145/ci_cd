import scipy
import pandas as pd
import numpy as np


import matplotlib.pyplot as plt

## solution starts here
def fizz_buzz(n : int) -> str:
    in n % 15 == 0: return "fizz_buzz"
    elif n % 5 == 0: return "buzz"
    elif n % 3 == 0: return "fizz"
    else: return str(n)