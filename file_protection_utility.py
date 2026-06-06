import base64

def protect_file():
    file_name = input("Enter the file name to protect: ")

    try:
        with open(file_name, "rb") as file:
            data = file.read()

        encoded_data = base64.b64encode(data)

        protected_file = "protected_" + file_name
        with open(protected_file, "wb") as file:
            file.write(encoded_data)

        print(f"File protected successfully!")
        print(f"Protected file saved as: {protected_file}")

    except FileNotFoundError:
        print("File not found!")

def restore_file():
    file_name = input("Enter the protected file name: ")

    try:
        with open(file_name, "rb") as file:
            encoded_data = file.read()

        decoded_data = base64.b64decode(encoded_data)

        restored_file = "restored_" + file_name.replace("protected_", "")
        with open(restored_file, "wb") as file:
            file.write(decoded_data)

        print(f"File restored successfully!")
        print(f"Restored file saved as: {restored_file}")

    except FileNotFoundError:
        print("File not found!")

while True:
    print("\n=== File Protection Utility ===")
    print("1. Protect File")
    print("2. Restore File")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        protect_file()
    elif choice == "2":
        restore_file()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")