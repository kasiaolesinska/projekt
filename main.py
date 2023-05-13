from DictEntry import *

name = input("Wprowadź imie: ")
surname = input("Wprowadz nazwisko: ")
date_array = ["dzień", "miesiąc", "rok"]
birthday_array = []

i = 0

while len(birthday_array) != 3:
    val = input(f"Wprowadź {date_array[i]} urodzenia: ")
    if val.isdigit():
        birthday_array.append(val)
        i += 1
    else:
        print("Niepoprawny format danych, spróbuj ponownie")

birthday = birthday_array[0] + "." + birthday_array[1] + "." + birthday_array[2]

birthplace = input("Wprowadz miejce urodzenia: ")
fav_books = []

print("Wprowadź tytuły swoich ulubionych książek: ")
while True:
    bookname = input()
    if bookname == 'Q' or bookname == 'q':
        break
    else:
        fav_books.append(bookname)
        print(f"książka {bookname} dodana do listy")

wpis = DictEntry(name, surname, birthday, birthplace, fav_books)
wpis.print_entry()