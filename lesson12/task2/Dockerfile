FROM ubuntu_hello:latest AS task2
# Set an environment variable
ENV MY_TEXT "Hello to DevOps World"

# Set argumment
#ARG DEBIAN_FRONTEND=noninteractive

#update image
#RUN apt update && apt upgrade -y

#install latest python
#RUN apt-get update && apt-get install -y software-properties-common gcc && \
#    add-apt-repository -y ppa:deadsnakes/ppa

#RUN apt-get update && apt-get install -y python3.12 python3-distutils python3-pip python3-apt


# Use the environment variable in the CMD instruction
CMD ["/usr/bin/python3", "-c", "import os; print(os.getenv('MY_TEXT'))"]
