FROM ubuntu:latest AS base
ARG DEBIAN_FRONTEND=noninteractive

#update image
RUN apt update && apt upgrade -y

#install latest python
RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y python3.12 python3-distutils python3-pip python3-apt

CMD ["/usr/bin/python3", "-c", "print('Hello World')"]
