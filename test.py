from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Пример дат
dates = [datetime.strptime('2004-01-01', '%Y-%m-%d'),
         datetime.strptime('2004-01-10', '%Y-%m-%d'),
         datetime.strptime('2004-01-20', '%Y-%m-%d')]

# Пример коэффициентов уравнения прямой
A = 2
B = -1
C = -5

# Функция для преобразования дат в числовые значения (например, количество дней с начала 2000 года)
def transform_date_to_numeric(date):
    start_date = datetime(2000, 1, 1)
    return (date - start_date).days

# Преобразуем даты в числовые значения
numeric_values = [transform_date_to_numeric(date) for date in dates]

# Генерируем значения x для построения прямой
x = np.array(numeric_values)
y = (-A * x - C) / B

# Строим график прямой
fig, ax = plt.subplots()
plt.plot(x, y, label='{}x + {}y + {} = 0'.format(A, B, C))

# Добавляем точки для каждой даты на прямой
for date, numeric_value in zip(dates, numeric_values):
    plt.scatter(numeric_value, (-A * numeric_value - C) / B, color='red', label=str(date))

plt.xlabel('Дата')
plt.ylabel('y')
plt.title('Прямая, заданная уравнением {}x + {}y + {} = 0 с показанными точками дат'.format(A, B, C))
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

# Настройка меток оси x
ax.xaxis.set_major_locator(mdates.DayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

plt.show()