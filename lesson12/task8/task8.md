# build web app and optimize build flow


docker build -t task8img .
docker run -p 8000:8000 --name task8 task8img




https://adevait.com/laravel/containerizing-laravel-applications-with-docker