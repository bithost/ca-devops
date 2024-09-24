# Ubuntu version: latest,22.04, 20.04
ARG UBNT_VERSION=20.04

FROM ubuntu:${UBNT_VERSION}

#this is required to skip questions during update/upgrade process.
ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install curl -y

