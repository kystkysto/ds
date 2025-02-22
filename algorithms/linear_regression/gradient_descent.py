import numpy as np

# 📌 ДАННЫЕ: рост, возраст → вес
X = np.array([
    [1.7, 25],
    [1.8, 30],
    [1.6, 20],
    [1.75, 35],
    [1.65, 40],
    [1.85, 45],
    [1.55, 18],
    [1.70, 29],
    [1.78, 33],
    [1.62, 21]
])
y = np.array([70, 80, 55, 78, 65, 90, 50, 74, 82, 58])  # Реальные веса

# 📌 1. ДЕЛИМ ДАННЫЕ ВРУЧНУЮ (80% train, 20% validation)
N = len(X)  # Общее количество данных
split_idx = int(N * 0.8)  # Индекс, на котором разделяем train и val

X_train, X_val = X[:split_idx], X[split_idx:]  # 80% в train, 20% в validation
y_train, y_val = y[:split_idx], y[split_idx:]  # 80% в train, 20% в validation

# 📌 2. Инициализируем случайные веса
w1, w2 = np.random.randn(), np.random.randn()
b = np.random.randn()

# 📌 3. Параметры обучения
learning_rate = 0.01
epochs = 1000
patience = 10  # Early Stopping (остановка при переобучении)
best_loss = float('inf')
no_improve_count = 0

# 📌 4. Функция потерь (MSE)
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# 📌 5. Градиентный спуск + Early Stopping
for epoch in range(epochs):
    y_pred = w1 * X_train[:, 0] + w2 * X_train[:, 1] + b  # Предсказание
    loss = mse(y_train, y_pred)  # Вычисляем ошибку

    # 📌 Градиенты
    dw1 = -2 * np.mean((y_train - y_pred) * X_train[:, 0])
    dw2 = -2 * np.mean((y_train - y_pred) * X_train[:, 1])
    db = -2 * np.mean(y_train - y_pred)

    # 📌 Обновляем веса
    w1 -= learning_rate * dw1
    w2 -= learning_rate * dw2
    b -= learning_rate * db

    # 📌 Early Stopping: проверяем, улучшилась ли модель
    if loss < best_loss:
        best_loss = loss
        no_improve_count = 0  # Сбрасываем счетчик
    else:
        no_improve_count += 1  # Увеличиваем счетчик, если улучшений нет

    if no_improve_count >= patience:
        print(f"🛑 Остановка на {epoch}-й эпохе: переобучение!")
        break

    # 📌 Выводим ошибку каждые 100 эпох
    if epoch % 100 == 0:
        print(f"Эпоха {epoch}, Ошибка: {loss:.3f}")

# 📌 6. Финальные веса
print(f"🎯 Обученные веса: w1={w1:.3f}, w2={w2:.3f}, b={b:.3f}")

# 📌 7. Оценка модели на тестовых данных (валидация)
y_val_pred = w1 * X_val[:, 0] + w2 * X_val[:, 1] + b
val_loss = mse(y_val, y_val_pred)
print(f"📊 Ошибка на валидационных данных (MSE): {val_loss:.3f}")

# 📌 8. Тестируем модель на новых данных
рост = 1.72
возраст = 28
предсказанный_вес = w1 * рост + w2 * возраст + b
print(f"🔮 Предсказанный вес для роста {рост}м и возраста {возраст} лет: {предсказанный_вес:.2f} кг")
