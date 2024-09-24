#!/bin/bash

# Function to check if the path exists and if it's a file or directory
check_path() {
    local path=$1
    if [ -e "$path" ]; then
        if [ -d "$path" ]; then
            echo "'$path' exists and is a directory."
        elif [ -f "$path" ]; then
            echo "'$path' exists and is a file."
        else
            echo "'$path' exists but is neither a regular file nor a directory."
        fi
    else
        echo "'$path' does not exist."
    fi
}

# Prompt the user to enter a path
read -p "Please enter the path: " user_path

# Check if the input is empty
if [ -z "$user_path" ]; then
    echo "No path provided. Exiting."
    exit 1
fi

# Call the function with the provided path
check_path "$user_path"
