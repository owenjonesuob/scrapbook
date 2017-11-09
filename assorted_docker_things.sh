### Get a docker container's IP address

# First get container ID
docker ps

# Then look under NetworkSettings
docker inspect <container ID>
