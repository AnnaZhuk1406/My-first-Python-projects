import random
print("Я загадав число від 1 до 10")
number = random.randint(1, 10)
attempts = 5 #
for i in range(attempts):
    guess_input(input(f"Спроба {i+1}")
"Введи своє число: ")
guess = int(input("Вгадуй число; "))
if guess == number:
    print(f"Ти вгадала!")
else:
        print("Ти не вгадала. Було число:",
number) #
input("Натисни Enter щоб закрити гру...")

        
