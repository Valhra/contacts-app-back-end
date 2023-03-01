import json

contacts = []

def AddContact():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contact = {
        'name': name,
        'surname': surname,
        'phone': phone,
        'email': email
    }

    contacts.append(contact)

def PrintContacts():
    for contact in contacts:
        print(f"{contact['name']}")

def SaveContacts():
    with open('contacts.json', 'w', encoding='UTF8') as file:
        contacts_dict = {
            'contacts': contacts
        }        
        json.dump(contacts_dict, file, indent=4)

def LoadContacts():
    # UZDEVUMS
    # izveido funkciju kas nolasīs datus no 
    # faila contacts.json uz sarakstu contacts
    with open('contacts.json', 'r', encoding='UTF8') as file:
        dict = json.load(file)
        return dict['contacts']

contacts = LoadContacts()
while(True):
    response = input("A-add contact, P-print, E-exit: ")
    
    if response == 'A':
        AddContact()
        SaveContacts()
    elif response == 'P':
        PrintContacts()           
    elif response == 'E':
        break
    