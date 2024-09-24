# run docker image with python, copy script and run it

docker build -t task3img .

docker run -it --name task3 task3img

docker rm -f task3