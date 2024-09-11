import string
import random
from datetime import datetime
from pprint import pprint


def is_verify_password(password: str) -> bool:
    if len(password) >= 8:
        is_len_pass = True
    else:
        is_len_pass = False

    is_have_digit = False
    is_have_char = False

    for char in password:
        if char.isalpha():
            is_have_char = True
        elif char.isdigit():
            is_have_digit = True

    if is_len_pass and is_have_digit and is_have_char:
        return True
    else:
        return False


def generate_password() -> str:
    while True:
        command = input("Потрібно створити пароль для можливості працювати в системі.\n"
                    "Введіть 1 - для введення свого паролю.\n"
                    "Введіть 2 - для автоматичної генерації паролю\n-> ")

        if command == "1":
            password = input("Введіть свій пароль. Довжина паролю має бути не менше 8 символіd, містити мінім одна буква та одну цифру.\n-> ")

            if is_verify_password(password):
                return password
            else:
                input("Ваш пароль не пройшов перевірку. Спробуйте ще раз. 'Enter' для продовження ")

        elif command == "2":
            string_password = string.ascii_lowercase + string.digits

            len_password = input("Введіть довжину паролю, мінім 8 символів: ")
            if len_password.isdigit() and int(len_password) > 8:
                len_password = int(len_password)
            else:
                len_password = 8

            is_upper = input("Чи використовувати великі літери для генерації паролю: 1 - так, будь який інший символ - ні -> ")
            if is_upper == "1":
                string_password += string.ascii_uppercase

            is_punctuation = input("Чи використовувати спецсимволи для генерації паролю: 1 - так, будь який інший символ - ні -> ")
            if is_punctuation == "1":
                string_password += string.punctuation

            is_repeat = input("Чи можуть символи у паролю повторюватись. 1 - так, будь який інший символ - ні -> ")
            if is_repeat == "1":
                password = random.choices(string_password, k=len_password)
            else:
                password = random.sample(string_password, k=len_password)

            return "".join(password)


animals = {
1:    "Кілер",
2:   "Катран",
3:   "Крістіан",
4:   "Кербер",
5:    "Дарлінг",
6:    "Рефлект",
7:    "Фарадей",
8:    "Діксон",
9:   "Арнольд",
10:    "Парнас"
}


def show_animals_cursed(animals: list) -> None:
    print(animals)
        
def add_animal_at_animals_cursed(animals: list) -> None:
                animals_cured = input("введить тварину яку хотите додати до списку ликування:")
                animals_cured.__add__(animals)
                print(f"дякую тварину додано до ликивання\nНатисніть 'enter' для продовження\n")

def animal_not_cursed():
    input(f"вашу тваринку вилiкувано заберить ее на кассе\nНатисніть 'enter' для продовження\n")

def show_any_all_cursed(animals_cursed: list) -> None:
    print(animals_cursed)

def exit():
    print(f"дакую що були з нами\nНатисніть 'enter' для продовження\n")
def delete_animal():
    input("введить тварину яку хотите видалити з ликування:")
    input("тварину було видалено\nНатисніть 'enter' для продовження\n")
def delete_animal_number():
    input("введить тварину за номером яку хотите видалити з ликування:")
    input("тварину було видалено\nНатисніть 'enter' для продовження\n")

def animals_sorted(animals: list) -> None:
    sorted_animals = sorted(animals)
    print(sorted_animals)
def reneme_animal():
    input("введить назву тварину для змини:")
    input("тварину им'я зминнено\nНатисніть 'enter' для продовження\n")
def show_animal_number():
    input("введить номер тварини щоб ее знайти")
    input(animals)
    input("\nНатисніть 'enter' для продовження\n")

animals_cursed = ["миша наркоман"]
commands = {
        "show_all_animals_cursed": "показать всех виликуваних тварин",         
        "add_animal_at_animals_cursed":"Додати нову тварину до списку на лікування",  
        "animal_not_cursed":"Тварину вилікувано",                          
        "show_any_all_cursed":"Показати список вилікуваних тварин",          
        "exit":"Вийти з програми",                            
        "delete_animal":"Видалити помилково додану тварину за ім'ям",
        "delete_animal_number":"Видалити помилково додану тварину за номером",
        "animals_sorted":"Відсортувати список тварин за ім'ям",
        "reneme_animal":"Змінити ім'я тварини",                       
        "show_animal_number":"Знайти номер тварини за ім'ям"
    }
pprint(commands,width=200)



















































































































