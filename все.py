# # east = ['корея', 'незнаю', 'ничего']
# # west = ['штото', 'америка', 'северная корея']
# # all = east + west
# # all.sort()
# # print(all)

# people = [["Андрій", "Собчук"], ["Микола", "Сутий"], ["Андрей", "чоловек"]]

# count = 0
# for person in people:
#     if person[0] == "Микола":
#         count += 1

# print(f"{count}")


# products = [
#     "Гречка",
#     "Макарони",
#     "Спагеті",
#     "Картопля",
#     "Буряк",
#     "Морква",
#     "Капуста",
#     "Цибуля",
#     "Часник",
#     "Борошно",
#     "Яйця",
#     "Соняшникова олія",
#     "Вершкове масло",
#     "Сіль",
#     "Перець",
#     "Цукор",
#     "Оцет",
#     "Сода",
#     "Чай",
#     "Кава"
# ]

# products_sold = []

# commands = [
#     "1. Показати список наявних товарів",
#     "2. Додати новий товар до списку",
#     "3. Додати список товарів",
#     "4. Видалити товар за ім'ям",
#     "5. Видалити товар за номер",
#     "6. Відсортувати список товарів за ім'ям",
#     "7. Продати товар",
#     "8. Знайти номер товару за ім'ям",
#     "9. Показати список проданих товарів",
#     "10. Показати історію продажів",
#     "11. Вийти з програми"
# ]

# while True:
#     for command in commands:
#         print(command)

#     command = input("\nВведіть номер команди: ")

#     if command == "1":
#         for i, product in enumerate(products, start=1):
#             print(f"{i}: {product}")

#         input("\nНатисніть 'enter' для продовження\n")

#     elif command == "2":
#         product = input("\nВведіть новий товар для додавання до списку: ")

#         if product in products:
#             input("\nТакий товар вже доданий\nНатисніть 'enter' для продовження\n")
#         else:
#             products.append(product)
#             input("\nНовий товар доданий до списку\nНатисніть 'enter' для продовження\n")

#     elif command == "3":
#         prods = input("\nВведіть список товарів через пробіл:\n").split()
#         products.extend(prods)
#         input("\nСписок продуктів розширено\nНатисніть 'enter' для продовження\n")

#     elif command == "4":
#         product = input("Введіть назву товару для видалення: ")

#         if product in products:
#             products.remove(product)
#             input(f"\nТовар '{product}' видалено зі списку\nНатисніть 'enter' для продовження\n")
#         else:
#             input(f"\nТовар '{product}' відсутній у списку\nНатисніть 'enter' для продовження\n")

#     elif command == "5":
#         number = input("Введіть номер товару для видалення: ")

#         if number.isdigit() and 0 < int(number) <= len(products):
#             product = products.pop(int(number) - 1)
#             input(f"\nТовар '{product}' видалено зі списку\nНатисніть 'enter' для продовження\n")
#         else:
#             input("\nВвели невірний номер")

#     elif command == "6":
#         prods = sorted(products)

#         for i, prod in enumerate(prods, start=1):
#             print(f"{i}: {prod}")

#         input("\nСписок товарі відсортовано\nНатисніть 'enter' для продовження\n")

#     elif command == "7":
#         product = input("Введіть товар для продажу: ")

#         if product in products:
#             products.remove(product)
#             products_sold.append(product)
#             input(f"Товар '{product}' продано\nНатисніть 'enter' для продовження\n")
#         else:
#             input(f"Товар '{product}' відсутній у списку")

#     elif command == "8":
#         product = input("Введіть назву товару для пошуку: ")

#         if product in products:
#             index = products.index(product)
#             input(f"\nТовар '{product}' знаходить під номер '{index + 1}'\nНатисніть 'enter' для продовження\n")
#         else:
#             input(f"\nТовар '{product}' відсутній у списку")

#     elif command == "9":
#         print("\nСписок проданий товарів\n")
#         for i, product in enumerate(products_sold, start=1):
#             print(f"{i}: {product}")

#         input("\nНатиснiть 'enter' для продовження\n")

#     elif command == "10":
#         prods_sold = products_sold[::-1]

#         if not prods_sold:
#             input("\nСписок проданих товарів порожній\n")

#         print("\nІсторія продажу\n")
#         for product in prods_sold:
#             print(product)

#         input("\nНатисніть 'enter' для продовження\n")

#     elif command =="11":
#         print("\nДякую що були з нами. Чекаємо наступної зустрічі.\n")
#         break






# clients = [
#     ['Василина Микитюк', 'провулок Петра Лещенка, буд. 523 кв. 70, Кременець, 88741', 41, 1],
#     ['Єлисей Архимович', "узвіз Грецька, буд. 91, Зимогір'я, 91927", 54, 2],
#     ['Ярослава Нестайко', 'парк Польовий 1-й, буд. 736, Бурштин , 41479', 23, 3],
#     ['Богуслава Адамчук', 'вулиця Овідіопольська дорога, буд. 67 кв. 841, Ірміно, 07762', 53, 4],
#     ['Анжела Уманець', 'вулиця Шахтинський, буд. 5, Бібрка, 10886', 46, 5],
#     ['Бабко Тереза Веніяминівна', 'шосе Бригадна, буд. 603, Харків, 32057', 36, 6],
#     ['Єва Шутько', 'парк Першотравневий 2-й, буд. 626 кв. 2, Часів Яр, 75588', 45, 7],
#     ['Коваленко Прохір Єфремович', "узвіз Гагаріна, буд. 199 кв. 102, Куп'янськ, 85166", 51, 8],
#     ['Герман Гаврюшенко', 'шосе Амурський 4-й, буд. 830 кв. 60, Теребовля, 53150', 26, 9],
#     ['Наталія Величко', 'вулиця Утьосова, буд. 850 кв. 40, Андрушівка, 83872', 34, 10],
#     ['Трохим Доценко', 'парк Вокзальний, буд. 75 кв. 8, Чернігів, 44698', 56, 11],
#     ['Амалія Затула', 'провулок Грецький, буд. 36 кв. 9, Стебник, 20012', 28, 12],
#     ['Валентин Петренко', 'сквер Олександра Невського, буд. 79, Благовіщенське, 87501', 23, 13],
#     ['Альбіна Штепа', 'шосе Джерельна, буд. 41, Могилів-Подільський, 52248', 46, 14],
#     ['Вікторія Алексійчук', 'узвіз Рівності, буд. 7, Мена , 89476', 21, 15],
#     ['Богданна Василенко', 'узвіз Станційна 1-ша, буд. 02 кв. 0, Ічня, 55112', 56, 16],
#     ['Ярина Піддубний', 'набережна Анни Ахматової, буд. 4 кв. 067, Бунге , 06871', 40, 17],
#     ['Семен Закусило', 'площа Пересипська 8-ма, буд. 013, Лутугине, 93047', 23, 18],
#     ['Данна Дерегус', 'вулиця Садова 6-та, буд. 639 кв. 52, Хуст, 88000', 56, 19],
#     ['Мазепа Оксана Орестівна', 'набережна Азербайджан, буд. 529 кв. 15, Устилуг, 97729', 24, 20],
#     ['Мілена Дубас', 'парк Героїв оборони Одеси, буд. 1 кв. 042, Бобровиця, 96367', 44, 21],
#     ['Георгій Дейнека', 'шосе Троїцька, буд. 4 кв. 997, Чуднів, 52554', 32, 22],
#     ['Галина Колісниченко', 'парк Савицький, буд. 67 кв. 410, Устилуг, 40922', 49, 23],
#     ['Анастасія Архипенко', 'парк 1-ша Лінія Марії Демченко, буд. 9 кв. 387, Новодружеськ, 13148', 40, 24],
#     ['Клавдія Гоголь-Яновський', 'площа Покровський, буд. 47 кв. 28, Кодима, 53683', 29, 25],
#     ['Михайлина Закусило', 'площа Аркадіївський, буд. 569 кв. 142, Бахчисарай, 06061', 41, 26],
#     ['Яків Дуплій', 'шосе Князівський, буд. 06, Шепетівка, 82791', 47, 27],
#     ['Алла Засядько', 'шосе Світлий, буд. 3 кв. 5, Нетішин, 71634', 46, 28],
#     ['Вікторія Байдак', 'узвіз Морський 2-й, буд. 0, Балта, 59419', 50, 29],
#     ['Мирослав Власенко', 'набережна Мічманський 2-й, буд. 61, Борщів, 57881', 28, 30],
#     ['Єлисавета Авраменко', 'узвіз Лобачевського, буд. 748 кв. 554, Шумськ, 43845', 39, 31],
#     ['Шеремет Антон Омелянович', 'парк Пестеля, буд. 9, Червоноград, 06815', 21, 32],
#     ['Ватаманюк Галина Русланівна', 'набережна Бородінська, буд. 39 кв. 64, Сєвєродонецьк, 67809', 59, 33],
#     ['Юстина Ярош', 'сквер Прокатна, буд. 946 кв. 5, Луцьк, 70868', 24, 34],
#     ['Василина Шамрай', 'парк Золотий берег, буд. 60 кв. 221, Южноукраїнськ, 09745', 49, 35],
#     ['Юстина Рудько', 'набережна Ключовий 1-й, буд. 1 кв. 859, Зеленодольськ, 20582', 37, 36],
#     ['Пріска Орлик', 'парк Міцкевича, буд. 44 кв. 32, Ялта, 41973', 28, 37],
#     ['Данило Яремчук', 'проспект 5-та Суворовська, буд. 3 кв. 4, Жданівка, 24388', 51, 38],
#     ['Богодар Перебийніс', 'узвіз Семінарська, буд. 22, Буча, 35788', 35, 39],
#     ['Дмитро Гаврилишин', 'шосе Аптекарський, буд. 0 кв. 83, Синельникове, 06821', 58, 40],
#     ['Ватаманюк Марія Аркадіївна', 'провулок Книжковий, буд. 233, Красилів, 57426', 56, 41],
#     ['Чуйко Петро Петрович', 'площа Ткачова, буд. 3 кв. 79, Алупка, 86736', 29, 42],
#     ['Світлана Стельмах', 'шосе Манежний, буд. 34 кв. 02, Калинівка , 85284', 33, 43],
#     ['Амалія Данькевич', 'шосе Поперечний, буд. 996, Батурин, 51683', 32, 44],
#     ['Марко Вовк', 'шосе Скляний 1-й, буд. 61, Перечин, 30237', 46, 45],
#     ['Віра Данилюк', 'парк Ямчитського, буд. 393 кв. 0, Бібрка, 02567', 24, 46],
# ['Валерій Непорожній', 'вулиця Лінія 33-тя, буд. 77, Марганець , 35926', 51, 47],
#     ['Одарка Талан', 'площа Богдана Хмельницького, буд. 9, Іллінці, 16593', 57, 48],
#     ['Симон Ященко', 'узвіз Дальній, буд. 129, Переяслав, 63109', 50, 49],
#     ['Ярослава Демʼяненко', 'набережна Чайковського, буд. 8, Зіньків, 69453', 51, 50]
#  ]



# rating_customers = []

# commands = [
#     "0. Вийти з програми",
#     "1. Показати актуальний список клієнтів",
#     "2. Клієнт виїжджає з номеру (надає оцінку обслуговування)",
#     "3. Клієнт переїжджає в інший номер",
#     "4. Новий клієнт",
#     "5. Змінити дані користувача",
#     "6. Відсортувати список клієнтів за ім'ям",
#     "7. Відсортувати список клієнтів за віком",
#     "8. Хто перебуває в номері",
#     "9. Показати відгуки",
#     "10. Показати вільні номери",
#     "11. Забронювати номер"
# ]





# while True:
#     for command in commands:
#         print(command)

#     command = input("Введіть номер команди: ")

#     if command == "0":
#         print("Дякую за Вашу роботу. До побачення")
#         break

#     elif command == "1":
#         for client in clients:
#             print(f"Клієнт '{client[0]}' перебуває у кімнаті № {client[-1]}")

#         input("\nНатисніть enter для продовження \n")

#     elif command == "2":
#         client_output = input("Введіть ім'я та призвіще клієнта: ")
#         rating = input("Введіть рейтинг від користувача в діапазоні 0-5: ")

#         for client in clients:
#             if client_output in client[0]:
#                 break
#         else:
#             input("\nТакий клієнта в готелі відсутній.\nНатисніть enter для продовження \n")
#             continue

#         clients.remove(client)
#         client.append(rating)
#         rating_customers.append(client)
#         input("\nКлієнта успішно видалено зі списку. Натисніть enter для продовження \n")

#     elif command == "3":
#         client_move = input("Введіть ім'я та призвіще клієнта: ")
#         room_number = input("Введіть номер кімнати в діпазоні 1-50: ")

#         if room_number.isdigit() and 1 <= int(room_number) <= 50:
#             for client in clients:
#                 if room_number == client[-1]:
#                     input("\nНомер зайнятий. Натисніть enter для продовження \n")
#                     break
#             else:
#                 for client in clients:
#                     if client_move in client[0]:
#                         client[-1] = room_number
#                         input("\nКлієнт переїхав. Натисніть enter для продовження \n")
#                         break
#         else:
#             input("\nНекоректно введені дані. Натисніть enter для продовження \n")

#     elif command == "9":
#         for customer in rating_customers:
#             print(customer)
#         input("\nНатисніть enter для продовження \n")


#     elif command == "10":
#             input("\nнаданий момент всi номери зайнятi,если што ми вам повидомим \n натиснить enter для продовження")
#             break
   
#     elif command == "11":
        
#         input("наданий момент вильний тiльки 105 номер на 5 етаже.\n нажмите enter для продовження")
#     break


# animals = [
#     "Кілер",
#     "Катран",
#     "Крістіан",
#     "Кербер",
#     "Дарлінг",
#     "Рефлект",
#     "Фарадей",
#     "Діксон",
#     "Арнольд",
#     "Парнас"
# ]

# animals_cured = []

# commands = [
#     "1. Показати список тварин на лікуванні",         # print(animals)
#     "2. Додати нову тварину до списку на лікування",  # animals.append(animal)
#     "3. Тварину вилікувано",                          # animals.remove(animal), animals_cured.append(animal)
#     "4. Показати список вилікуваних тварин",          # print(animals_cured)
#     "5. Вийти з програми",                            # break
# #############################################################################################################
#     "6. Видалити помилково додану тварину за ім'ям",
#     "7. Видалити помилково додану тварину за номером",
#     "8. Відсортувати список тварин за ім'ям",
#     "9. Змінити ім'я тварини",                        # Видалити та вставити на її місце іншу (animals.insert(0, animal))
#     "10. Знайти номер тварини за ім'ям"
# ]

# while True:
#     for command in commands:
#         print(commands)

#     command = input("Введіть номер команди: ")

#     if command == "1":
#         print("animals")
#         break


#     elif command == '2':
#         animals.remove(animals), animals_cured.append(animals)





                                            




# one_line_text = '''я лублу 8  какат утром, днем,и 8 вечером после 0  окрошки и огурца.'''

# new_string = ""
# for char in one_line_text:
#     if not char.isdigit():
#         new_string += char

# print(new_string)



# string = "чоловек яйко"

# count = 0
# char = ""

# for c in string:
#     if count < string.count(c):
#         count = string.count(c)
#         char = c

# print(f"Символ '{char}' зустрічається в нашому речені '{count}' разів")





# for i in range(1, 101):
#     if i % 2 == 1:
#         print(i)

# for i in range(1, 101):
#  summ =+ i 
# if i % 2 == 1:
#         print(summ)


# def longest_word(sentence):
#     words = sentence.split()
#     longest = ""
    
#     for word in words:
    
#         if len(word) > len(longest):
#             longest = word
    
#     return longest
# sentence = "Дано рядок, який містить довільне речення, слова в якому розділені пробілами"
# print(longest_word(sentence))

# import string
# import random


# PRODUCTS = [
#     "Гречка",
#     "Макарони",
#     "Спагеті",
#     "Картопля",
#     "Буряк",
#     "Морква",
#     "Капуста",
#     "Цибуля",
#     "Часник",
#     "Борошно",
#     "Яйця",
#     "Соняшникова олія",
#     "Вершкове масло",
#     "Сіль",
#     "Перець",
#     "Цукор",
#     "Оцет",
#     "Сода",
#     "Чай",
#     "Кава"
# ]

# PRODUCTS_SOLD = []

# PASSWORD = ""

# COMMANDS = [
#     "1. Показати список наявних товарів",
#     "2. Додати новий товар до списку",
#     "3. Додати список товарів",
#     "4. Видалити товар за ім'ям",
#     "5. Видалити товар за номер",
#     "6. Відсортувати список товарів за ім'ям",
#     "7. Продати товар",
#     "8. Знайти номер товару за ім'ям",
#     "9. Показати список проданих товарів",
#     "10. Показати історію продажів",
#     "11. Вийти з програми",
#     "12. Написати відгук",         ######################################
#     "13. Знайти групи символів, які повторюються (використовуючи всі відгуки)",    ############################
#     "14. Знайти продукти, які є паліндромами"            ################################
# ]

# while not PASSWORD:
#     command = input("Потрібно створити пароль для можливості працювати в системі.\n"
#                     "Введіть 1 - для введення свого паролю.\n"
#                     "Введіть 2 - для автоматичної генерації паролю\n-> ")

#     if command == "1":
#         password = input("Введіть свій пароль. Довжина паролю має бути не менше 8 символіd, містити мінім одна буква та одну цифру.\n-> ")

#         if len(password) >= 8:
#             is_len_pass = True
#         else:
#             is_len_pass = False

#         is_have_digit = False
#         is_have_char = False

#         for char in password:
#             if char.isalpha():
#                 is_have_char = True
#             elif char.isdigit():
#                 is_have_digit = True

#         if is_len_pass and is_have_digit and is_have_char:
#             PASSWORD = password
#         else:
#             input("Ваш пароль не пройшов перевірку. Спробуйте ще раз. 'Enter' для проовження ")

#     elif command == "2":
#         string_password = string.ascii_lowercase + string.digits

#         len_password = input("Введіть довжину паролю, мінім 8 символів: ")
#         if len_password.isdigit() and int(len_password) > 8:
#             len_password = int(len_password)
#         else:
#             len_password = 8

#         is_upper = input("Чи використовувати великі літери для генерації паролю: 1 - так, будь який інший символ - ні -> ")
#         if is_upper == "1":
#             string_password += string.ascii_uppercase

#         is_punctuation = input("Чи використовувати спецсимволи для генерації паролю: 1 - так, будь який інший символ - ні -> ")
#         if is_punctuation == "1":
#             string_password += string.punctuation

#         is_repeat = input("Чи можуть символи у паролю повторюватись. 1 - так, будь який інший символ - ні -> ")
#         if is_repeat == "1":
#             password = random.choices(string_password, k=len_password)
#         else:
#             password = random.sample(string_password, k=len_password)

#         PASSWORD = "".join(password)

# else:
#     input(f"\nПароль успішно створено: '{PASSWORD}'. Запам'ятайте його. 'Enter' для продовження ")

# password = input("\nВведіть пароль для входу у систему: ")

# while password == PASSWORD:
#     for command in COMMANDS:
#         print(command)

#     command = input("\nВведіть номер команди: ")

#     if command == "1":
#         for i, product in enumerate(PRODUCTS, start=1):
#             print(f"{i}: {product}")

#         input("\nНатисніть 'enter' для продовження\n")

#     elif command == "2":
#         product = input("\nВведіть новий товар для додавання до списку: ")

#         if product in PRODUCTS:
#             input("\nТакий товар вже доданий\nНатисніть 'enter' для продовження\n")
#         else:
#             PRODUCTS.append(product)
#             input("\nНовий товар доданий до списку\nНатисніть 'enter' для продовження\n")

#     elif command == "3":
#         prods = input("\nВведіть список товарів через пробіл:\n").split()
#         PRODUCTS.extend(prods)
#         input("\nСписок продуктів розширено\nНатисніть 'enter' для продовження\n")

#     elif command == "4":
#         product = input("Введіть назву товару для видалення: ")

#         if product in PRODUCTS:
#             PRODUCTS.remove(product)
#             input(f"\nТовар '{product}' видалено зі списку\nНатисніть 'enter' для продовження\n")
#         else:
#             input(f"\nТовар '{product}' відсутній у списку\nНатисніть 'enter' для продовження\n")

#     elif command == "5":
#         number = input("Введіть номер товару для видалення: ")

#         if number.isdigit() and 0 < int(number) <= len(PRODUCTS):
#             product = PRODUCTS.pop(int(number) - 1)
#             input(f"\nТовар '{product}' видалено зі списку\nНатисніть 'enter' для продовження\n")
#         else:
#             input("\nВвели невірний номер")

#     elif command == "6":
#         prods = sorted(PRODUCTS)

#         for i, prod in enumerate(prods, start=1):
#             print(f"{i}: {prod}")

#         input("\nСписок товарі відсортовано\nНатисніть 'enter' для продовження\n")

#     elif command == "7":
#         product = input("Введіть товар для продажу: ")

#         if product in PRODUCTS:
#             PRODUCTS.remove(product)
#             PRODUCTS_SOLD.append(product)
#             input(f"Товар '{product}' продано\nНатисніть 'enter' для продовження\n")
#         else:
#             input(f"Товар '{product}' відсутній у списку")

#     elif command == "8":
#         product = input("Введіть назву товару для пошуку: ")

#         if product in PRODUCTS:
#             index = PRODUCTS.index(product)
#             input(f"\nТовар '{product}' знаходить під номер '{index + 1}'\nНатисніть 'enter' для продовження\n")
#         else:
#             input(f"\nТовар '{product}' відсутній у списку")

#     elif command == "9":
#         print("\nСписок проданий товарів\n")
#         for i, product in enumerate(PRODUCTS_SOLD, start=1):
#             print(f"{i}: {product}")

#         input("\nНатисніть 'enter' для продовження\n")

#     elif command == "10":
#         prods_sold = PRODUCTS_SOLD[::-1]

#         if not prods_sold:
#             input("\nСписок проданих товарів порожній\n")

#         print("\nІсторія продажу\n")
#         for product in prods_sold:
#             print(product)

#         input("\nНатисніть 'enter' для продовження\n")

#     elif command =="11":
#         print("\nДякую що були з нами. Чекаємо наступної зустрічі.\n")
#         break
   

#     elif command == "12":
#         input("ви можете здесь написать свiй видгук")




# else:
#     print("\nПароль введено не вірно. Доступ заборонено.")



# import string
# import random


# PRODUCTS = [
#     "Гречка",
#     "Макарони",
#     "Спагеті",
#     "Картопля",
#     "Буряк",
#     "Морква",
#     "Капуста",
#     "Цибуля",
#     "Часник",
#     "Борошно",
#     "Яйця",
#     "Соняшникова олія",
#     "Вершкове масло",
#     "Сіль",
#     "Перець",
#     "Цукор",
#     "Оцет",
#     "Сода",
#     "Чай",
#     "Кава"
# ]

# PRODUCTS_SOLD = []

# REVIEWS = ['чудовий день', 'незнанаю',]
# PASSWORD = ""

# COMMANDS = [
#     "1. Показати список наявних товарів",
#     "2. Додати новий товар до списку",
#     "3. Додати список товарів",
#     "4. Видалити товар за ім'ям",
#     "5. Видалити товар за номер",
#     "6. Відсортувати список товарів за ім'ям",
#     "7. Продати товар",
#     "8. Знайти номер товару за ім'ям",
#     "9. Показати список проданих товарів",
#     "10. Показати історію продажів",
#     "11. Вийти з програми",
#     "12. Написати відгук",         ######################################
#     "13. Знайти групи символів, які повторюються (використовуючи всі відгуки)",    ############################
#     "14. Знайти продукти, які є паліндромами"            ################################
# ]

# while not PASSWORD:
#     command = input("Потрібно створити пароль для можливості працювати в системі.\n"
#                     "Введіть 1 - для введення свого паролю.\n"
#                     "Введіть 2 - для автоматичної генерації паролю\n-> ")

#     if command == "1":
#         password = input("Введіть свій пароль. Довжина паролю має бути не менше 8 символіd, містити мінім одна буква та одну цифру.\n-> ")

#         if len(password) >= 8:
#             is_len_pass = True
#         else:
#             is_len_pass = False

#         is_have_digit = False
#         is_have_char = False

#         for char in password:
#             if char.isalpha():
#                 is_have_char = True
#             elif char.isdigit():
#                 is_have_digit = True

#         if is_len_pass and is_have_digit and is_have_char:
#             PASSWORD = password
#         else:
#             input("Ваш пароль не пройшов перевірку. Спробуйте ще раз. 'Enter' для проовження ")

#     elif command == "2":
#         string_password = string.ascii_lowercase + string.digits

#         len_password = input("Введіть довжину паролю, мінім 8 символів: ")
#         if len_password.isdigit() and int(len_password) > 8:
#             len_password = int(len_password)
#         else:
#             len_password = 8

#         is_upper = input("Чи використовувати великі літери для генерації паролю: 1 - так, будь який інший символ - ні -> ")
#         if is_upper == "1":
#             string_password += string.ascii_uppercase

#         is_punctuation = input("Чи використовувати спецсимволи для генерації паролю: 1 - так, будь який інший символ - ні -> ")
#         if is_punctuation == "1":
#             string_password += string.punctuation

#         is_repeat = input("Чи можуть символи у паролю повторюватись. 1 - так, будь який інший символ - ні -> ")
#         if is_repeat == "1":
#             password = random.choices(string_password, k=len_password)
#         else:
#             password = random.sample(string_password, k=len_password)

#         PASSWORD = "".join(password)

# else:
#     input(f"\nПароль успішно створено: '{PASSWORD}'. Запам'ятайте його. 'Enter' для продовження ")

# password = input("\nВведіть пароль для входу у систему: ")

# while password == PASSWORD:
#     for command in COMMANDS:
#         print(command)

#     command = input("\nВведіть номер команди: ")

#     if command == "1":
#         for i, product in enumerate(PRODUCTS, start=1):
#             print(f"{i}: {product}")

#         input("\nНатисніть 'enter' для продовження\n")

#     elif command == "2":
#         product = input("\nВведіть новий товар для додавання до списку: ")

#         if product in PRODUCTS:
#             input("\nТакий товар вже доданий\nНатисніть 'enter' для продовження\n")
#         else:
#             PRODUCTS.append(product)
#             input("\nНовий товар доданий до списку\nНатисніть 'enter' для продовження\n")

#     elif command == "3":
#         prods = input("\nВведіть список товарів через пробіл:\n").split()
#         PRODUCTS.extend(prods)
#         input("\nСписок продуктів розширено\nНатисніть 'enter' для продовження\n")

#     elif command == "4":
#         product = input("Введіть назву товару для видалення: ")

#         if product in PRODUCTS:
#             PRODUCTS.remove(product)
#             input(f"\nТовар '{product}' видалено зі списку\nНатисніть 'enter' для продовження\n")
#         else:
#             input(f"\nТовар '{product}' відсутній у списку\nНатисніть 'enter' для продовження\n")

#     elif command == "5":
#         number = input("Введіть номер товару для видалення: ")

#         if number.isdigit() and 0 < int(number) <= len(PRODUCTS):
#             product = PRODUCTS.pop(int(number) - 1)
#             input(f"\nТовар '{product}' видалено зі списку\nНатисніть 'enter' для продовження\n")
#         else:
#             input("\nВвели невірний номер")

#     elif command == "6":
#         prods = sorted(PRODUCTS)

#         for i, prod in enumerate(prods, start=1):
#             print(f"{i}: {prod}")

#         input("\nСписок товарі відсортовано\nНатисніть 'enter' для продовження\n")

#     elif command == "7":
#         product = input("Введіть товар для продажу: ")

#         if product in PRODUCTS:
#             PRODUCTS.remove(product)
#             PRODUCTS_SOLD.append(product)
#             input(f"Товар '{product}' продано\nНатисніть 'enter' для продовження\n")
#         else:
#             input(f"Товар '{product}' відсутній у списку")

#     elif command == "8":
#         product = input("Введіть назву товару для пошуку: ")

#         if product in PRODUCTS:
#             index = PRODUCTS.index(product)
#             input(f"\nТовар '{product}' знаходить під номер '{index + 1}'\nНатисніть 'enter' для продовження\n")
#         else:
#             input(f"\nТовар '{product}' відсутній у списку")

#     elif command == "9":
#         print("\nСписок проданий товарів\n")
#         for i, product in enumerate(PRODUCTS_SOLD, start=1):
#             print(f"{i}: {product}")

#         input("\nНатисніть 'enter' для продовження\n")

#     elif command == "10":
#         prods_sold = PRODUCTS_SOLD[::-1]

#         if not prods_sold:
#             input("\nСписок проданих товарів порожній\n")

#         print("\nІсторія продажу\n")
#         for product in prods_sold:
#             print(product)

#         input("\nНатисніть 'enter' для продовження\n")

#     elif command =="11":
#         print("\nДякую що були з нами. Чекаємо наступної зустрічі.\n")
#         break
   
#     elif command =="12":    
#         text = input("можете тут оставить свой отзив:")
#         REVIEWS.append(text)

#     elif command =="13":

#         REWIEWS = input("Введіть рядок тексту: ")
#         words = REWIEWS.split()  
#         repeated_words = []


#         for word in words:
    
#          if words.count(word) > 1 and word not in repeated_words:
#             repeated_words.append(word)


#             print("Слова, які зустрічаються більше одного разу:", repeated_words)
    

#     elif command =="14":
#         input("в етом списке нету продуктiв палiндроммами \n Натисніть 'enter' для продовження\n "  )















































































































































































































































































































































































































































































































































































































































































































































































































































































































    


