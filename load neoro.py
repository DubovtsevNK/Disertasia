from typing import List, Any, Union

import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.layers import Dense
from keras.models import load_model

model = load_model("my_model.h5")
#model = load_model("model01.h5")
print(model.get_weights())
finish=1
while finish:
    a = float(input('a'))
    b = float(input('b'))
    c = float(input('c'))
    d = float(input('d'))
    print(model.predict([[a,b,c,d]]))
    #print(model.predict([[a, b]]))
    finish = int(input("finish?"))