def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().casefold()
    return cmd, *args

def add_contact(args, contacts):
    try: 
        name, phone = args   
        if name.isdigit():
            return f"The name cannot be a number"
        if name in contacts: 
            return f"Contact with the name {name} already exists"            
        else: 
            contacts[name] = phone            
            return "Contact added"
    except Exception as e:
        return f'Input error: {e}. The right command format: add name phone'

def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone            
            return "Contact updated"
        else: 
            return f"There is no contact with the name {name}"
    except Exception as e:
        return f'Input error: {e}. The right command format: change name phone'

def show_phone(args, contacts):
    try:
        name = args[0]        
        if name in contacts:
            phone = contacts.get(name) 
            return f"The phone number for the contact {name} is  {phone}"
        else:
            return f"There is no contact with the name {name}"
    except Exception as e:
        return f'Input error: {e}. The right command format: phone name'
    
def show_all(contacts):
    print(contacts)
    return "All contacts showed"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)        

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args,contacts))

        elif command == "change":
            print(change_contact(args,contacts))

        elif command == "phone":
            print(show_phone(args,contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()