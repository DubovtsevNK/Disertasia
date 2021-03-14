from typing import List, Any, Union

import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.layers import Dense
zad = list()

f = open("data.xls", "r")
zad_float = []
ych_float: List[Union[Union[List[Any], list], Any]] = []
for line in f:
    zad.append((line.strip().split(";")))

for element_list in zad:
    list_fl = []
    list_ych = []
    list_fl.append(float(element_list[0]))#/7)
    list_fl.append(float(element_list[1]))#/10)
    list_fl.append(float(element_list[3]))#/35)
#    list_fl.append(float(element_list[3]))  # /35)
    list_ych.append(float(element_list[2]))#/35)
    # for element in element_list:
    #     list_fl.append(float(element))
    zad_float.append(list_fl)
    ych_float.append(list_ych)
# zad_float.append([1,0.7,0])
# ych_float.append([0.8])

f.close()

# print(zad_float)
# print(ych_float)
# c = np.array(zad_float , ndmin=3).T
# f = np.array(ych_float).T

cd = np.array(zad_float)
cf = np.array(ych_float)

print(cd)

print(cf)
model = keras.Sequential()
model.add(Dense(4, input_shape=(3,), activation='tanh'))
model.add(Dense(4,activation='tanh'))
model.add(Dense(1,activation='tanh'))

model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.1))

log = model.fit(cd, cf, batch_size=32, epochs=70)

plt.plot(log.history['loss'])
plt.grid(True)
plt.show()
test_acc=model.evaluate(cd,cf, batch_size=32)
print("test acc:", test_acc)
finish = 1

# while finish:
#     a = float(input('a'))
#     b = float(input('b'))
#     c = float(input('c'))
#     print(model.predict([[a,b,c]]))
#     finish = int(input("finish?"))

print(model.get_weights())
otevt = input("Сохранить модель? y|n")
if otevt == "y":
    model.save("my_model.h5")

