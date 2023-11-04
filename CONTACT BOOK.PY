contacts = {}

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contact_id = len(contacts) + 1
    contacts[contact_id] = {'name': name, 'phone': phone, 'email': email, 'address': address}
    print(f"Contact '{name}' has been added with ID {contact_id}")

def view_contact_list():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for contact_id, contact_info in contacts.items():
            print(f"ID: {contact_id}, Name: {contact_info['name']}, Phone: {contact_info['phone']}")

def search_contact():
    search_term = input("Enter a name or phone number to search: ")
    found_contacts = []
    for contact_id, contact_info in contacts.items():
        if search_term in contact_info['name'] or search_term in contact_info['phone']:
            found_contacts.append((contact_id, contact_info))
    if not found_contacts:
        print("No matching contacts found.")
    else:
        print("Matching Contacts:")
        for contact_id, contact_info in found_contacts:
            print(f"ID: {contact_id}, Name: {contact_info['name']}, Phone: {contact_info['phone']}")

def update_contact():
    contact_id = int(input("Enter the ID of the contact to update: "))
    if contact_id in contacts:
        name = input("New Name (or press Enter to keep it unchanged): ")
        phone = input("New Phone (or press Enter to keep it unchanged): ")
        email = input("New Email (or press Enter to keep it unchanged): ")
        address = input("New Address (or press Enter to keep it unchanged): ")
        if name:
            contacts[contact_id]['name'] = name
        if phone:
            contacts[contact_id]['phone'] = phone
        if email:
            contacts[contact_id]['email'] = email
        if address:
            contacts[contact_id]['address'] = address
        print(f"Contact with ID {contact_id} has been updated.")
    else:
        print("Contact not found.")

def delete_contact():
    contact_id = int(input("Enter the ID of the contact to delete: "))
    if contact_id in contacts:
        del contacts[contact_id]
        print(f"Contact with ID {contact_id} has been deleted.")
    else:
        print("Contact not found.")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
