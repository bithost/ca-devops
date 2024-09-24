#!/bin/bash

# Function to recursively count files and directories
count_items() {
    local dir_path=$1

    # Check if the provided path is a valid directory
    if [ ! -d "$dir_path" ]; then
        echo "'$dir_path' is not a valid directory."
        exit 1
    fi

    # Count the number of files and directories
    local file_count=$(find "$dir_path" -type f | wc -l)
    local dir_count=$(find "$dir_path" -type d | wc -l)

    echo "In directory '$dir_path':"
    echo "Number of files: $file_count"
    echo "Number of directories: $dir_count"
}

# If no arguments are provided, prompt the user for the directory path
if [ $# -eq 0 ]; then
    read -p "Please enter the directory path: " dir_path
else
    dir_path=$1
fi

# Call the function to count files and directories
count_items "$dir_path"
