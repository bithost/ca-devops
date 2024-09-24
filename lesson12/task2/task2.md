# Modify Docker file to use ENV values

docker build -t task2img .

docker rm -f task2

docker run -it --name task2 task2img