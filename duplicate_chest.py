import re
# Скрипт выводит дубликаты координат с указанием локаций
# Параметры
file_path = "chest_list.txt"  # Укажите путь к файлу
tolerance = 0.003  # Погрешность для поиска дубликатов

# Функция для извлечения координат из строки
def extract_coordinates(text):
    matches = re.findall(r"\{([\d.]+),([\d.]+)\}", text)
    return [(float(x), float(y)) for x, y in matches]

# Читаем файл и обрабатываем данные
data = {}
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        match = re.match(r'(\w+)=\{(.+)\}', line)
        if match:
            name = match.group(1)  # Название локации
            coordinates = extract_coordinates(match.group(2))  # Координаты
            data[name] = coordinates

# Поиск дубликатов
duplicates = []
checked = set()

for name, coords in data.items():
    for i, (x1, y1) in enumerate(coords):
        for j, (x2, y2) in enumerate(coords):
            if i != j and (j, i, name) not in checked:  # Исключаем повторные проверки
                if abs(x1 - x2) <= tolerance and abs(y1 - y2) <= tolerance:
                    duplicates.append((name, (x1, y1), (x2, y2)))
                checked.add((i, j, name))

# Вывод результата
if duplicates:
    print("Найдены дубликаты с погрешностью", tolerance)
    for name, coord1, coord2 in duplicates:
        print(f"Локация: {name}, Координаты: {coord1} ≈ {coord2}")
else:
    print("Дубликаты не найдены.")
