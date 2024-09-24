# Docker file for node.js as. Use Docker buildkit to pass secret file during the build time using --secret flag


Do we need this?
export DOCKER_BUILDKIT=1

Internet is saying, that BuildKit is on by default

# Build the Docker image
docker build -t task7img .

# Create a Docker secret from the secret.txt file
echo "secure_key" | docker secret create my_secret -

# Run the container, mounting the secret
docker run -d -p 3000:3000 --secret id=secrets,src=secret.txt task7img
