import re
import json

# Читаем файл
with open("raw.txt", "r", encoding="utf-8") as f:
    data = f.read()

# 1. Извлекаем данные через RegEx
date_val = re.search(r"\d{2}\.\d{2}\.\d{4}", data).group()
time_val = re.search(r"\d{2}:\d{2}", data).group()
# Находим товары: (Название) ... (Цена)
items = re.findall(r"([А-Яа-я]+)\s\.+\s(\d+\.\d{2})", data)
payment = re.search(r"оплаты:\s([А-Яа-я]+)", data).group(1)

# 2. Формируем структуру и считаем общую сумму (Task 3)
products = [{"name": n, "price": float(p)} for n, p in items]
total_sum = sum(item["price"] for item in products)

# 3. Итоговый объект (Task 6)
result = {
    "date": date_val, 
    "time": time_val,
    "products": products,
    "total_amount": total_sum,
    "payment_method": payment
}

# Вывод в формате JSON
print(json.dumps(result, indent=4, ensure_ascii=False))


