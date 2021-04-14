from typing import List, Any, Union

import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.layers import Dense
import mat4py as m4p

zad = list()

# f = open("data.xls", "r")
zad_float = [[0, 0], [0, 1], [1, 0], [1, 1]]
ych_float = [[0], [1], [1], [0]]

# print(zad_float)
# print(ych_float)


cd = np.array(zad_float)
cf = np.array(ych_float)

print(cd)

print(cf)
model = keras.Sequential()
model.add(Dense(4, input_shape=(2,), activation='sigmoid'))
model.add(Dense(4, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.1))

# tensorboard_cbk = keras.callbacks.TensorBoard(log_dir='/full_path_to_your_logs')
# keras.callbacks.TensorBoard(
#   log_dir='/full_path_to_your_logs',
#   histogram_freq=0,  # Как часто писать лог визуализаций гистограмм
#   embeddings_freq=0,  # Как часто писать лог визуализаций вложений
#   update_freq='epoch')  # Как часто писать логи (по умолчанию: однажды за эпоху)
# log = model.fit(cd, cf, batch_size=32, epochs=50,callbacks=[tensorboard_cbk])
log = model.fit(cd, cf, batch_size=32, epochs=100)
plt.plot(log.history['loss'])
plt.grid(True)
plt.ylabel('Loss')
plt.xlabel('Epohs')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# first_layer_weights = model.layers[0].get_weights()[0]
# np.savez('test.mat',first_layer_weights)
# first_layer_biases  = model.layers[0].get_weights()[1]
# second_layer_weights = model.layers[1].get_weights()[0]
# second_layer_biases  = model.layers[1].get_weights()[1]
#
# dataW1 = {'w1' : model.layers[0].get_weights()[0].tolist()}
# dataB1 = {'b1' : model.layers[0].get_weights()[1].tolist()}
# dataW2 = {'w2' : model.layers[1].get_weights()[0].tolist()}
# dataB2 = {'b2' : model.layers[1].get_weights()[1].tolist()}
# m4p.savemat('w1.mat', dataW1)
# m4p.savemat('b1.mat', dataB1)
# m4p.savemat('w2.mat', dataW2)
# m4p.savemat('b2.mat', dataB2)

# print(first_layer_weights)
print(model.get_weights())
# otevt = input("Сохранить модель и файлы? y|n")
# if otevt == "y":
#     model.save("model01.h5")

print(model.predict([[1, 0]]))
