
contacts = {}

while True:
    print("\n--- PHONEBOOK MENU ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contacts[name] = {
            "Phone": phone,
            "Email": email
        }
        print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Name:", name)
            print("Phone:", contacts[name]["Phone"])
            print("Email:", contacts[name]["Email"])
        else:
            print("Contact not found!")

    elif choice == "3":
        name = input("Enter name to update: ")

        if name in contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")

            contacts[name]["Phone"] = phone
            contacts[name]["Email"] = email

            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "5":
        if contacts:
            for name, details in contacts.items():
                print("\nName:", name)
                for key, value in details.items():
                    print(key + ":", value)
        else:
            print("Phonebook is empty!")

    elif choice == "6":
        print("Exiting Phonebook...")
        break

    else:
        print("Invalid choice! Try again.")