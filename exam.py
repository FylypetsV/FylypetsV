try:
    numerator = float(input("Введіть чисельник: "))
    denominator = float(input("Введіть знаменник: "))

    result = numerator / denominator

    print("Результат ділення:", result)

except ZeroDivisionError:
    print("Помилка: Ділення на нуль неможливе.")
except ValueError:
    print("Помилка: Введені дані не є числами.")
except Exception as e:
    print("Сталася помилка:", e)
