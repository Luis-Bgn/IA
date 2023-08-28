import random

# Define los datos de entrada y salida de la compuerta AND
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 0, 0, 1]

# Inicializa los pesos aleatorios
w = [random.random(), random.random()]
#Sesgos
b = random.random()

lr = 0.5
intentos = 1000

for epoch in range(intentos):
    for i in range(len(X)):
        # Realiza la predicción
        Y = w[0] * X[i][0] + w[1] * X[i][1] + b
        a = 1 if Y >= 0 else 0

        # Calcula el error y actualiza los pesos y el sesgo
        error = y[i] - a
        w[0] += lr * error * X[i][0]
        w[1] += lr * error * X[i][1]
        b += lr * error

# Utiliza la neurona para predecir los valores de la compuerta AND
print("0 AND 0 =", 1 if w[0] * 0 + w[1] * 0 + b >= 0 else 0)
print("0 AND 1 =", 1 if w[0] * 0 + w[1] * 1 + b >= 0 else 0)
print("1 AND 0 =", 1 if w[0] * 1 + w[1] * 0 + b >= 0 else 0)
print("1 AND 1 =", 1 if w[0] * 1 + w[1] * 1 + b >= 0 else 0)