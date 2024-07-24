import random


def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Я загадал число от 1 до 100. Попробуй отгадать!")

    while not guessed:
        user_guess = input("Введите ваше число:")

        try:
            user_guess = int(user_guess)
            attempts += 1

            if user_guess < number_to_guess:
                print("Загаданное число больше.")
            elif user_guess > number_to_guess:
                print("Загаданное число меньше.")
            else:
                guessed = True
                print(f"Вы угадали число! {number_to_guess} за {attempts} попыток.")

        except ValueError:
            print("Пожалуйста, введите корректное число")


if __name__ == "__main__":
    guess_the_number()
