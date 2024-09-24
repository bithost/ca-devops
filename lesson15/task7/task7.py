import json

def print_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    print("Current data:")
    for i, (key, value) in enumerate(data.items(), start=1):
        print(f"{i}. {key}: {value}")

def remove_block(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    print("Current data:")
    for i, (key, value) in enumerate(data.items(), start=1):
        print(f"{i}. {key}: {value}")

    try:
        block_to_remove = int(input("Enter the number of the block to remove: "))
        if 1 <= block_to_remove <= len(data):
            key_to_remove = list(data.keys())[block_to_remove - 1]
            del data[key_to_remove]
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=2)
            print(f"The block with key '{key_to_remove}' has been removed.")
        else:
            print("Invalid block number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def add_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    print("Current data:")
    for i, (key, value) in enumerate(data.items(), start=1):
        print(f"{i}. {key}: {value}")

    new_key = input("Enter the key for the new data: ")
    new_value = input("Enter the value for the new data: ")

    data[new_key] = new_value

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

    print(f"New data with key '{new_key}' has been added.")

def main():
    file_path = 'task7.json'

    while True:
        print("\nMenu:")
        print("1. Print JSON file")
        print("2. Remove block from JSON file")
        print("3. Add data to JSON file")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print_json(file_path)
        elif choice == '2':
            remove_block(file_path)
        elif choice == '3':
            add_data(file_path)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
