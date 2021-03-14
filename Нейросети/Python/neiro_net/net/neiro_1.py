import numpy
# библиотека scipy.special содержит сигмоиду expit()
import scipy.special


# определение класса нейронной сети
class neuralNet:
    # инициализация нейронной сети
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        self.inodes = input_nodes  # количество узлов входного слоя
        self.hnodes = hidden_nodes  # количество узлов скрытого слоя
        self.onodes = output_nodes  # количество узлов выходного слоя
        self.lr = learning_rate  # коэффициент обучения
        # Матрицы весовых коэффициентов связей wih (между входным и скрытым
        # слоями) и who (между скрытым и выходным слоями).
        # Весовые коэффициенты связей между узлом i и узлом j следующего слоя
        # обозначены как w_i_j:
        # wll w21
        # wl2 w22 и т.д.
        self.wih = (numpy.random.rand(self.hnodes, self.inodes) - 0.5)
        self.who = (numpy.random.rand(self.onodes, self.hnodes) - 0.5)
        # использование сигмоиды в качестве функции активации
        self.activation_function = lambda x: scipy.special.expit(x)
        pass

    # тренировка
    def train(self, inputs_list, targets_list):
        # преобразовать список входных значений в двухмерный массив
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T
        # рассчитать входящие сигналы для скрытого слоя
        hidden_inputs = numpy.dot(self.wih, inputs)
        # рассчитать исходящие сигналы для скрытого слоя
        hidden_outputs = self.activation_function(hidden_inputs)
        # рассчитать входящие сигналы для выходного слоя
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # рассчитать исходящие сигналы для выходного слоя
        final_outputs = self.activation_function(final_inputs)
        output_errors = targets - final_outputs
        # ошибки скрытого слоя - это ошибки output_errors,
        # распределенные пропорционально весовым коэффициентам связей
        # и рекомбинированные на скрытых узлах
        hidden_errors = numpy.dot(self.who.T, output_errors)
        # обновить весовые коэффициенты связей между скрытым и выходным слоями
        self.who += self.lr * numpy.dot((output_errors * final_outputs *
                                        (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs *
                                         (1.0 - hidden_outputs)), numpy.transpose(inputs))

    # опрос
    def query(self, inputs_list):
        # преобразовать список входных значений
        # в двухмерный массив
        inputs = numpy.array(inputs_list, ndmin=2).T
        # рассчитать входящие сигналы для скрытого слоя
        hidden_inputs = numpy.dot(self.wih, inputs)
        # рассчитать исходящие сигналы для скрытого слоя
        hidden_outputs = self.activation_function(hidden_inputs)
        # рассчитать входящие сигналы для выходного слоя
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # рассчитать исходящие сигналы для выходного слоя
        final_outputs = self.activation_function(final_inputs)
        return final_outputs


# бинарное сложение
input_nodes = 2
hidden_nodes = 1000
output_nodes = 2
learn_rate = 0.25

n = neuralNet(input_nodes, hidden_nodes, output_nodes, learn_rate)
inputs_list=["0.99, 0.99", "0.01, 0.99", "0.99, 0.01", "0.01, 0.01"]
targets_list=["0.99, 0.01","0.99, 0.01","0.99, 0.01", "0.01, 0.99"]
number = len(inputs_list)
for e in range(0, 100):
    for i in range(0,number):
        inputs=numpy.asfarray(inputs_list[i].split(','))
        targets=numpy.asfarray(targets_list[i].split(','))
        n.train(inputs, targets)


test=["1, 1",  "0, 0","1, 0", "0, 1"]
test_res=["0.99, 0.01","0.01, 0.99","0.99, 0.01", "0.99, 0.01"]
for i in range(0,4):
    res=n.query(numpy.asfarray(test[i].split(',')))
    print(res)
    print(test_res[i])
