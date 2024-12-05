from backup_restore import backup_contacts, restore_contacts
from backup_restore import all_contacts


def add_contact():
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = int(input("Enter phone number: "))
    address = input("Enter address: ")

    for contact in all_contacts:
        if contact['contact_phone'] == phone:
            print("Error: Phone number already exists, try with another one.")
            return

    contact_book = {
        'contact_name': name,
        'contact_email': email,
        'contact_phone': phone,
        'contact_address': address
    }

    all_contacts.append(contact_book)

    backup_contacts()

    print('contact added successfully!')


def view_all_contact():
    try:
        for contact in all_contacts:
            print(
                contact['contact_name'],
                contact['contact_email'],
                contact['contact_phone'],
                contact['contact_address'],
                sep=' | ')

    except:
        print('No contact available to view!')


def search_by_name():
    try:
        search_term = input('Enter contact name: ')

        for contact in all_contacts:
            if search_term == contact['contact_name']:
                print(f"Found: {contact['contact_name']} - {contact['contact_phone']}")

        else:
            print('No such contact available!')

    except:
        print('No such contact available!')


def search_by_phone():
    try:
        search_term = input('Enter contact phone: ')

        for contact in all_contacts:
            if search_term == contact['contact_phone']:
                print(f"Found: {contact['contact_name']} - {contact['contact_phone']}")

        else:
            print('No such contact available!')

    except:
        print('No such contact available!')


def remove_contact():
    search_term = input('Enter name to search to remove: ')

    for index, contact in enumerate(all_contacts):
        if search_term.lower() in contact['contact_name'].lower():
            print(f"{index + 1}. {contact['contact_name']} - {contact['contact_phone']}")

    selected_index = int(input('Enter a contact number to remove: '))

    all_contacts.pop(selected_index - 1)

    print('Contact removed successfully!')


print('Welcome!')

menu_text = """
Your options:
1. Add contact
2. View all contact
3. Search by name
4. Search by phone
5. Remove contact
0. Exit
"""


def main_menu():
    restore_contacts()

    while True:

        print(menu_text)
        choice = input('Enter your choice: ')

        if choice == '1':
            add_contact()

        elif choice == '2':
            view_all_contact()

        elif choice == '3':
            search_by_name()

        elif choice == '4':
            search_by_phone()

        elif choice == '5':
            remove_contact()

        elif choice == '0':
            break

        else:
            print('Wrong choice!')


main_menu()
