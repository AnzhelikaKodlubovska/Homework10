from collections import UserDict

class Field:
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError("Invalid value")
        self.value = value

    def __str__(self):
        return str(self.value)

    def is_valid(self, value):
        return True


class Name(Field):
    pass


class Phone(Field):
    def is_valid(self, value):
        return len(str(value)) == 10 and str(value).isdigit()


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone):
        for p in self.phones:
            if str(p.value) == str(phone):
                self.phones.remove(p)
                break

    def edit_phone(self, old_phone, new_phone):
        phone_to_edit = self.find_phone(old_phone)
        if phone_to_edit:
            phone_to_edit.value = new_phone
        else:
            raise ValueError("Phone number not found")

    def find_phone(self, phone):
        for p in self.phones:
            if str(p.value) == str(phone):
                return p
        return None


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True
        else:
            return False
