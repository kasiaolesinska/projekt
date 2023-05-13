class DictEntry:

    def __init__(self, name, surname, birthday, birth_place, fav_books):
        self.__name = name
        self.__surname = surname
        self.__birthday = birthday
        self.__birth_place = birth_place
        self.__fav_books = fav_books

    def print_entry(self):
        print(f"Imię: {self.__name}\nNazwisko: {self.__surname}\nData urodzenia: {self.__birthday}\n"
              f"Miejsce urodzenia: {self.__birth_place}")
        print("Ulubione książki: ")
        for book in self.__fav_books:
            print(f"- {book}")