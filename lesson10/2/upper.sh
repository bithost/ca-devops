#!/bin/bash

# Function to convert a string to uppercase
to_uppercase() {
    local input="$1"
    echo "$input" | tr '[:lower:]' '[:upper:]'
}

# Prompt the user for input
read -p "Please enter your text: " user_input

# Call the function with the provided input
result=$(to_uppercase "$user_input")
echo "Uppercase version: $result"
