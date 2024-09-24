#!/bin/bash

# Function to copy all .txt files from source to destination
copy_text_files() {
    local src_dir=$1
    local dest_dir=$2

    # Check if source directory exists
    if [ ! -d "$src_dir" ]; then
        echo "Source directory '$src_dir' does not exist."
        exit 1
    fi

    # Check if destination directory exists, if not create it
    if [ ! -d "$dest_dir" ]; then
        echo "Destination directory '$dest_dir' does not exist. Creating it."
        mkdir -p "$dest_dir"
    fi

    # Copy .txt files from source to destination
    cp "$src_dir"/*.txt "$dest_dir" 2>/dev/null

    if [ $? -eq 0 ]; then
        echo "All .txt files have been copied from '$src_dir' to '$dest_dir'."
    else
        echo "No .txt files found in '$src_dir'."
    fi
}

# Prompt the user to enter the source directory
read -p "Please enter the source directory: " source_directory

# Prompt the user to enter the destination directory
read -p "Please enter the destination directory: " destination_directory

# Call the function to copy .txt files
copy_text_files "$source_directory" "$destination_directory"
