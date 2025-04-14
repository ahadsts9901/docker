# 🚢 Learning Docker
## [Youtube Tutorial](https://www.youtube.com/watch?v=OhnTMWmfTBE)

## Some useful commands

| Command | Example | Description |
|---------|---------|-------------|
| `docker build .` | `docker build .` | Builds a Docker image from the current directory |
| `docker image list` | `docker image list` | Lists all Docker images on your system |
| `docker run IMAGE_ID` | `docker run d4a111255d32` | Runs a container from the specified image (foreground mode) |
| `docker run -it IMAGE_ID` | `docker run -it d4a111255d32` | Runs a container in interactive mode with terminal access |
| `docker stop CONTAINER_NAME` | `docker stop my-app` | Stops a running container |
| `docker ps` | `docker ps` | Lists only the running containers |
| `docker ps -a` | `docker ps -a` | Lists all containers (running and stopped) |
| `docker run -p HOST:CONTAINER IMAGE` | `docker run -p 5173:5173 my-app` | Maps a container port to a port on the host machine |
| `docker run -d -p HOST:CONTAINER IMAGE` | `docker run -d -p 5173:5173 my-app` | Runs a container in the background (detached mode) |
| `docker run -d --rm -p HOST:CONTAINER IMAGE` | `docker run -d --rm -p 5173:5173 my-app` | Runs a container in the background and removes it after it exits |
| `docker run -d --rm --name NAME -p HOST:CONTAINER IMAGE` | `docker run -d --rm --name vite-container -p 5173:5173 my-app` | Runs a container with a custom name, in background, and auto-removes on exit |
| `docker rm CONTAINER_NAME` | `docker rm vite-container` | Deletes a stopped container |
| `docker tag OLD NEW` | `docker tag myapp:latest myusername/myapp:1.0` | Tags an image with a new name or version |
