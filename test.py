import numpy as np


# Сигмоида
def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


# набор входных данных
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# выходные данные
y = np.array([[0, 0, 1, 1]]).T

# сделаем случайные числа более определёнными
np.random.seed(1)

# инициализируем веса случайным образом со средним 0
syn0 = 2 * np.random.random((3, 1)) - 1

for iter in range(10000):
    # прямое распространение
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))

    # насколько мы ошиблись?
    l1_error = y - l1

    # перемножим это с наклоном сигмоиды
    # на основе значений в l1
    l1_delta = l1_error * nonlin(l1, True)  # !!!

    # обновим веса
    syn0 += np.dot(l0.T, l1_delta)  # !!!

# Матрица весов сети. syn0 означает «synapse zero». Так как у нас всего два слоя, вход и выход, нам нужна одна
# матрица весов, которая их свяжет. Её размерность (3, 1), поскольку у нас есть 3 входа и 1 выход. Иными словами,
# l0 имеет размер 3, а l1 – 1. Поскольку мы связываем все узлы в l0 со всеми узлами l1, нам требуется матрица
# размерности (3, 1).

# Заметьте, что она инициализируется случайным образом, и среднее значение равно нулю. За этим стоит достаточно
# сложная теория. Пока просто примем это как рекомендацию. Также заметим, что наша нейросеть – это и есть эта самая
# матрица. У нас есть «слои» l0 и l1, но они представляют собой временные значения, основанные на наборе данных.
# Мы их не храним. Всё обучение хранится в syn0.


print ("Выходные данные после тренировки:")
print (l1)