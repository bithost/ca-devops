#!/bin/sh
set -e

# Perform any pre-start configurations here (optional)

# Print a message to indicate the start of the Python script
echo "Starting Python Script Task 4"

# Run the hello.py Python script
python3 hello.py

# Optionally, you might run other commands or processes here after running the script

# Keep the container running by using an infinite loop (if needed)
#while true; do
#    sleep 1
#done
