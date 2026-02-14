# Command-Line Contact Book Application
FILE_NAME = "contacts.txt"

def add_contact():
    name = input("Enter Name: ").strip()
    while True:
        phone = input("Enter Phone Number: ").strip()
        if phone.isdigit() and len(phone) == 10:
            break
        else:
            print("Invalid phone number! It must contain exactly 10 digits.\n")
    email = input("Enter Email: ").strip()
    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("Contact added successfully!\n")

def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()
        if not contacts:
            print("No contacts found.\n")
            return
        contacts.sort()
        print("\nSr No | Name | Phone | Email")
        print("------------------------------------------")
        sr_no = 1
        for contact in contacts:
            name, phone, email = contact.strip().split(",")
            print(sr_no, "|", name, "|", phone, "|", email)
            sr_no += 1
        print()
    except FileNotFoundError:
        print("No contact file found.\n")

def search_contact():
    search_name = input("Enter name to search: ").lower()
    found = False
    try:
        with open(FILE_NAME, "r") as file:
            for contact in file:
                name, phone, email = contact.strip().split(",")
                if search_name in name.lower():
                    print(f"\nContact Found:")
                    print(f"Name: {name}, Phone: {phone}, Email: {email}\n")
                    found = True
                    break
        if not found:
            print("Contact not found.\n")
    except FileNotFoundError:
        print("No contact file found.\n")

def delete_contact():
    delete_name = input("Enter name to delete: ").strip().lower()
    updated_contacts = []
    found = False
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()
        for contact in contacts:
            name, phone, email = contact.strip().split(",")
            if delete_name in name.strip().lower():
                found = True
                continue 
            else:
                updated_contacts.append(contact)
        if found:
            with open(FILE_NAME, "w") as file:
                file.writelines(updated_contacts)
            print("Contact deleted successfully!\n")
        else:
            print("Contact not found.\n")
    except FileNotFoundError:
        print("No contact file found.\n")

def main():
    while True:
        print("=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            delete_contact()
        elif choice == 5:
            print("Exiting application. Thank you!")
            break
        else:
            print("Invalid choice. Try again.\n")
main()
