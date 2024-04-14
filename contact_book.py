# contact book using python

contacts = []

def add_contacts():
    name = input("Enter name: ")
    number = input("Enter number: ")
    contacts.append({"name":name,"number":number})
    print("Contact added successfully")

def view_contacts():
    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("No contacts added.")

def search_contacts():
    name = input("Enter a name to search: ")
    found = False
    for contact in contacts:
        if contact["name"] == name:
            print(contact)
            found = True
    if not found:
        print("Contact not found")

while True:
    print("\n1.Add Contact\n2.View Contacts\n3.Search contact\n4.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contacts()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contacts()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
