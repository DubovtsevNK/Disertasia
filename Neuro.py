from typing import List, Any, Union

import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.layers import Dense
import mat4py as m4p
zad = list()

f = open("data.xls", "r")
zad_float = []
ych_float: List[Union[Union[List[Any], list], Any]] = []
for line in f:
    zad.append((line.strip().split(";")))

for element_list in zad:
    list_fl = []
    list_ych = []
    list_fl.append(float(element_list[0]))#)    #0-UZ\1
    #list_fl.append(float(element_list[1]))#/10)   #1-U\2
    #list_fl.append(float(element_list[2]))#/35)  #2 - Unc
    list_fl.append(float(element_list[3]))  # /35) #3 - oldU
    #list_fl.append(float(element_list[4]))  # /35) #4 - dU\45
    #list_fl.append(float(element_list[5]))  # /35) #5 - t
    list_fl.append(float(element_list[6]))  # /35) #6 - deltaU
    #list_fl.append(float(element_list[7]))  # /35) #6 - oldU2
    list_ych.append(float(element_list[2]))#/35)   #2 - Unc
    # for element in element_list:
    #     list_fl.append(float(element))
    zad_float.append(list_fl)
    ych_float.append(list_ych)
#zad_float.append([1,0,0,0])
#ych_float.append([0.8])

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
model.add(Dense(15, input_shape=(3,), activation='relu',use_bias=False))
model.add(Dense(8,activation='relu',use_bias=False))
model.add(Dense(1,activation='tanh',use_bias=False))

    model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.1))

log = model.fit(cd, cf, batch_size=32, epochs=10)

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
    dataW1 = {'w1': model.layers[0].get_weights()[0].tolist()}
    dataB1 = {'b1': model.layers[0].get_weights()[1].tolist()}
    dataW2 = {'w2': model.layers[1].get_weights()[0].tolist()}
    dataB2 = {'b2': model.layers[1].get_weights()[1].tolist()}
    dataW3 = {'w3': model.layers[2].get_weights()[0].tolist()}
    dataB3 = {'b3': model.layers[2].get_weights()[1].tolist()}
    m4p.savemat('w1.mat', dataW1)
    m4p.savemat('b1.mat', dataB1)
    m4p.savemat('w2.mat', dataW2)
    m4p.savemat('b2.mat', dataB2)
    m4p.savemat('w3.mat', dataW3)
    m4p.savemat('b3.mat', dataB3)
    model.save("my_model.h5")

