#!/bin/bash

create_directory_and_file() {
    local dir_name="$1"
    local file_name="$2"

    # Check if directory already exists
    if [ -d "$dir_name" ]; then
        echo "Directory '$dir_name' already exists."
        return
    fi

    # Create the directory
    mkdir -p "$dir_name"

    # Create the file inside the directory
    touch "$dir_name/$file_name"

    echo "Created directory '$dir_name' and file '$file_name'."
}

# Prompt the user for input
read -p "Please enter the folder name: " folder_name
read -p "Please enter the file name: " file_name

# Validate input (non-empty names)
if [ -z "$folder_name" ] || [ -z "$file_name" ]; then
    echo "Both folder name and file name must be provided."
    exit 1
fi

# Call the function with the provided arguments
create_directory_and_file "$folder_name" "$file_name"
