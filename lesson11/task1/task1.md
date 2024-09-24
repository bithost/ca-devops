# Create a container and run it

 sudo docker build -t php_hello_world .

 docker run --rm -d -p 80:80/tcp php_hello_world:latest 