def findName(name, phonebook):
    if name in phonebook:
        del phonebook[name]
        print(f"Deleted {name}'s phone number from the phonebook.")
    else:
        print(f"{name} not found in the phonebook.")

# Example phonebook dictionary
phonebook = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Eve": "555-123-4567"
}

name_to_delete = "Bob"
findName(name_to_delete, phonebook)

print(phonebook)  # Updated phonebook after deletion