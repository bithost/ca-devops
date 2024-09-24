import yaml

def print_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    print("Current data:")
    for i, student in enumerate(data['students'], start=1):
        print(f"{i}. {student['name']}: {student}")

def remove_block(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    print("Current data:")
    for i, student in enumerate(data['students'], start=1):
        print(f"{i}. {student['name']}: {student}")

    try:
        block_to_remove = int(input("Enter the number of the block to remove: "))
        if 1 <= block_to_remove <= len(data['students']):
            del data['students'][block_to_remove - 1]
            with open(file_path, 'w') as file:
                yaml.dump(data, file, default_flow_style=False)
            print(f"The block with number '{block_to_remove}' has been removed.")
        else:
            print("Invalid block number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def add_data(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    print("Current data:")
    for i, student in enumerate(data['students'], start=1):
        print(f"{i}. {student['name']}: {student}")

    new_student = {
        'name': input("Enter the name for the new student: "),
        'age': int(input("Enter the age for the new student: ")),
        'grade': input("Enter the grade for the new student: "),
        'subjects': input("Enter subjects for the new student (comma-separated): ").split(', ')
    }

    data['students'].append(new_student)

    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

    print(f"New data for student '{new_student['name']}' has been added.")

def main():
    file_path = 'task8.yaml'

    while True:
        print("\nMenu:")
        print("1. Print YAML file")
        print("2. Remove block from YAML file")
        print("3. Add data to YAML file")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print_yaml(file_path)
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
