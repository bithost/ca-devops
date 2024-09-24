# Ubuntu image that installs python and run script to display hello world

docker build -t ubuntu_hello .


docker run -it --name hello ubuntu_hello