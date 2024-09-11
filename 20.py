from datetime import datetime
from pprint import pprint

from src.password import generate_password
from src.products import {

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



def show_animals_cursed():
    with open("animals.cursed", "r", encoding="utf-8") as file:
        string = file.read()
        
def add_animal_at_animals_cursed():
    with open("animals.cursed", "w", encoding="utf-8") as file:
        string = file.write()

def animal_not_cursed():
    with open("animals.cursed", "r", encoding="utf-8") as file:
        string = file.read()

def exit():
    print(f"дакую що були з нами\nНатисніть 'enter' для продовження\n")
def delete_animal():
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














































































































