print("🧮 Калькулятор")
a = float(input("Введи перше число: "))
b = float(input("Введи друге число: "))
print("Оберіть дію:")
print("+ додавання")
print("- віднімання")
print("* множення")
print("/ ділення")
op = input("Введи знак дії: ")
if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b == 0:
        print("❌ На нуль ділити не можна")
        result = None
    else:
        result = a / b
else:
    print("❌ Невідома дія")
    result = None
if result is not None:
    print(f"✅ Результат: {result}")
input("Натисни Enter, щоб вийти...")
