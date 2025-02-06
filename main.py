import json

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file, default=lambda x: x.__dict__)

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            address_book = cls()
            for contact_data in data["contacts"]:
                contact = Person(contact_data["name"], contact_data["email"], contact_data["phone"], contact_data["favorite"])
                address_book.add_contact(contact)
            return address_book

    def search(self, query):
        results = []
        for contact in self.contacts:
            if query in contact.name or query in contact.phone:
                results.append(contact)
        return results

class Person:
    def __init__(self, name, email, phone, favorite):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

if __name__ == "__main__":
    address_book = AddressBook()

    contact1 = Person("John Doe", "john@example.com", "(123) 456-7890", False)
    contact2 = Person("Jane Smith", "jane@example.com", "(987) 654-3210", True)
    address_book.add_contact(contact1)
    address_book.add_contact(contact2)

    address_book.save_to_file("data.json")

    loaded_address_book = AddressBook.load_from_file("data.json")

    query = "John"
    results = loaded_address_book.search(query)
    for result in results:
        print(f"Name: {result.name}, Phone: {result.phone}")