import json

# Define the contact book class
class ContactBook:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        try:
            with open('contacts.json', 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []

    def save_contacts(self):
        with open('contacts.json', 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email, address):
        self.contacts.append({
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        })
        self.save_contacts()

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

    def search_contact(self, search_term):
        results = [c for c in self.contacts if search_term.lower() in c['name'].lower() or search_term in c['phone']]
        if results:
            for contact in results:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
        else:
            print("No contacts found.")

    def update_contact(self, name, phone=None, email=None, address=None):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                if phone:
                    contact['phone'] = phone
                if email:
                    contact['email'] = email
                if address:
                    contact['address'] = address
                self.save_contacts()
                print("Contact updated.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        self.contacts = [c for c in self.contacts if c['name'].lower() != name.lower()]
        self.save_contacts()
        print("Contact deleted.")

# Command-line interface
def main():
    book = ContactBook()
    
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            book.add_contact(name, phone, email, address)
        
        elif choice == '2':
            book.view_contacts()
        
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            book.search_contact(search_term)
        
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number (or leave blank): ")
            email = input("Enter new email (or leave blank): ")
            address = input("Enter new address (or leave blank): ")
            book.update_contact(name, phone if phone else None, email if email else None, address if address else None)
        
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            book.delete_contact(name)
        
        elif choice == '6':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
