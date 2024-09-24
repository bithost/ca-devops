# Use an Ubuntu base image
FROM ubuntu:latest

# Create a directory for the application
RUN mkdir -p /usr/src/app

# Copy the secret content into a file within the container
RUN --mount=type=secret,id=mysecret, src=secret-file, target=secret-file \
    echo "$(cat /run/secrets/mysecret)" > /usr/src/app/mysecret.txt

# Command to display the secret content at runtime
#CMD cat /usr/src/app/mysecret.txt
