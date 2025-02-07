# 📌 Линейная регрессия в Jupyter Notebook

# **Импортируем библиотеки**
import numpy as np
import matplotlib.pyplot as plt

# **1. Создаем данные: рост, возраст → вес**
X = np.array([
    [1.7, 25], [1.8, 30], [1.6, 20], [1.75, 35],
    [1.65, 40], [1.85, 45], [1.55, 18], [1.70, 29],
    [1.78, 33], [1.62, 21]
])
y = np.array([70, 80, 55, 78, 65, 90, 50, 74, 82, 58])

# **2. Разделяем данные на train и validation (80% / 20%)**
N = len(X)
split_idx = int(N * 0.8)
X_train, X_val = X[:split_idx], X[split_idx:]
y_train, y_val = y[:split_idx], y[split_idx:]

# **3. Инициализируем случайные веса**
w1, w2 = np.random.randn(), np.random.randn()
b = np.random.randn()

# **4. Определяем параметры обучения**
learning_rate = 0.01
epochs = 1000
losses = []  # Список для хранения значений ошибки

# **5. Функция потерь (MSE)**
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# **6. Обучение модели с визуализацией процесса**
for epoch in range(epochs):
    # Предсказание значений по текущим весам
    y_pred = w1 * X_train[:, 0] + w2 * X_train[:, 1] + b
    loss = mse(y_train, y_pred)
    losses.append(loss)
    
    # Вычисление градиентов
    dw1 = -2 * np.mean((y_train - y_pred) * X_train[:, 0])
    dw2 = -2 * np.mean((y_train - y_pred) * X_train[:, 1])
    db = -2 * np.mean(y_train - y_pred)
    
    # Обновление весов
    w1 -= learning_rate * dw1
    w2 -= learning_rate * dw2
    b -= learning_rate * db
    
    # Вывод ошибки каждые 100 эпох
    if epoch % 100 == 0:
        print(f"Эпоха {epoch}, Ошибка: {loss:.3f}")

# **7. График снижения ошибки (Loss Curve)**
plt.figure(figsize=(8, 5))
plt.plot(losses, label='MSE Loss', color='blue')
plt.xlabel('Эпохи')
plt.ylabel('Ошибка')
plt.title('График снижения ошибки')
plt.legend()
plt.show()

# **8. Оценка модели на тестовых данных (валидация)**
y_val_pred = w1 * X_val[:, 0] + w2 * X_val[:, 1] + b
val_loss = mse(y_val, y_val_pred)
print(f"📊 Ошибка на валидационных данных (MSE): {val_loss:.3f}")

# **9. Тестируем модель на новых данных**
рост = 1.72
возраст = 28
предсказанный_вес = w1 * рост + w2 * возраст + b
print(f"🔮 Предсказанный вес для роста {рост}м и возраста {возраст} лет: {предсказанный_вес:.2f} кг")
