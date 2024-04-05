from collections import UserDict
from datetime import datetime, timedelta
from time import strptime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

# class Phone(Field):
#     def __init__(self, value):
#         if not value.isdigit() or len(value) != 10:
#             raise ValueError
#         super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError
        self.__value = value


class Birthday(Field):
    def __init__(self, value):
        try:
            self.date = datetime.strptime(value, "%d./%m./%Y").date()
            super().__init__(value)
        except:
            raise ValueError
        
    def add_birthday(self, birthday):
        pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        if not new_phone.isdigit() or len(new_phone) != 10:
            raise ValueError
        
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday) # TODO: перевірити правильність запису та додати нову логіку додавання до книги

    def show_birthday(self, birthday): #TODO: зробити функцію
        pass 

    def birthdays(self): #TODO: зробити функцію
        pass


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def find_next_weekday(self, weekday):
        pass

    def get_upcoming_birthday(self, days=7):
        pass


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except ValueError:
            return "There is no such number in the database"
        
        except KeyError:
            return "There is no such user in the database"
        
        except IndexError:
            return "Index out of range"
    return wrapper


def parse_input(user_input): # TODO: переробити функцію
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book: AddressBook): # TODO: переробити функцію
    name, phone = args
    if name not in book:
        raise ValueError("Contact")
    book[name] = phone
    return "Contact updated successfully"

@input_error
def show_contact(args, contacts): # TODO: переробити функцію
    name = args[0]
    if name in contacts:
        return contacts[name]

@input_error
def show_all_contacts(book: AddressBook): # TODO: переробити функцію
    if book:
        return book
    else:
        return "No contacts found"
    
def add_birthday(args, book: AddressBook): #TODO: зробити функцію
    pass

def birthdays(args, book: AddressBook): #TODO: зробити функцію
    pass

def show_birthday(args, book: AddressBook): #TODO: зробити функцію
    pass




















book = AddressBook()