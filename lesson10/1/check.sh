#!/bin/bash

check_file_permissions() {
    local filename="$1"

    if [ ! -e "$filename" ]; then
        echo "File '$filename' does not exist."
        return
    fi

    # Check readability
    if [ -r "$filename" ]; then
        echo "File '$filename' is readable."
    else
        echo "File '$filename' is not readable."
    fi

    # Check writability
    if [ -w "$filename" ]; then
        echo "File '$filename' is writable."
    else
        echo "File '$filename' is not writable."
    fi

    # Check executability
    if [ -x "$filename" ]; then
        echo "File '$filename' is executable."
    else
        echo "File '$filename' is not executable."
    fi
}

check_file_permissions "$1"