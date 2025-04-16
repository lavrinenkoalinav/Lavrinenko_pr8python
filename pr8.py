
def task1_filtered_numbers():
    return [x for x in range(1, 101) if x % 3 == 0 and x % 5 != 0]

def task2_celsius_to_fahrenheit(celsius_list):
    return [c * 9 / 5 + 32 for c in celsius_list]

def task3_even_squares():
    return [x**2 for x in range(1, 51) if x % 2 == 0]

def task4_word_lengths(text):
    return [len(word) for word in text.split()]

def task5_composite_numbers():
    return [
        num for num in range(2, 101)
        if len([div for div in range(1, num + 1) if num % div == 0]) > 2
    ]

print("Завдання 1. Числа від 1 до 100, які кратні 3, але не кратні 5:")
print(task1_filtered_numbers())

print("\nЗавдання 2. Температури у Фаренгейтах:")
celsius = [0, 10, 20, 30, 40, 100]
print(task2_celsius_to_fahrenheit(celsius))

print("\nЗавдання 3. Квадрати парних чисел від 1 до 50:")
print(task3_even_squares())

print("\nЗавдання 4. Довжини слів у рядку:")
text = "Python is amazing and powerful language"
print(task4_word_lengths(text))

print("\nЗавдання 5. Складні числа від 1 до 100:")
print(task5_composite_numbers())
