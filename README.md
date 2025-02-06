# SerializableAddressBook

SerializableAddressBook is a Python project that allows users to manage an address book with contact information (name, email, phone number, and favorite status). The contacts are stored in a JSON file, making the data persistent and easily retrievable.

## Features

- **Add contacts**: Users can add contacts to the address book.
- **Save to file**: The address book can be saved to a JSON file for later use.
- **Load from file**: The address book can be loaded from a previously saved JSON file.
- **Search contacts**: Users can search for contacts by name or phone number.

## Technologies Used

- **Python**: The core programming language used to develop the application.
- **JSON**: Used for storing contact data persistently in a human-readable format.

## How It Works

1. **Add Contact**: The `add_contact()` method allows you to add a contact to the address book.
2. **Save to File**: The `save_to_file()` method saves the address book to a JSON file.
3. **Load from File**: The `load_from_file()` class method loads the address book from a JSON file.
4. **Search**: The `search()` method lets you search for contacts by their name or phone number.

## Getting Started

### Prerequisites

- Python 3.x
- No external dependencies required.

### Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/paulmusquaro/SerializableAddressBook.git
    ```

2. Navigate into the project directory:
    ```bash
    cd SerializableAddressBook
    ```

3. You can now use the project by running the Python file:
    ```bash
    python main.py
    ```

### Usage

1. Create an instance of the `AddressBook` class.
2. Add contacts using the `add_contact()` method.
3. Save the address book to a file using the `save_to_file()` method.
4. Load the address book from a file using `load_from_file()`.
5. Search for contacts by name or phone using the `search()` method.

### Example

```python
address_book = AddressBook()

contact1 = Person("John Doe", "john@example.com", "(123) 456-7890", False)
contact2 = Person("Jane Smith", "jane@example.com", "(987) 654-3210", True)

address_book.add_contact(contact1)
address_book.add_contact(contact2)

address_book.save_to_file("address_book.json")

loaded_address_book = AddressBook.load_from_file("address_book.json")
results = loaded_address_book.search("John")

for result in results:
    print(f"Name: {result.name}, Phone: {result.phone}")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
