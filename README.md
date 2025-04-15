# 🚢 Learning Docker
## [Youtube Tutorial](https://www.youtube.com/watch?v=OhnTMWmfTBE)
<img src="https://miro.medium.com/v2/resize:fit:882/1*Ibnwjo9LtUFxRY1MZgOcvg.png" width="320" />
<br />

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

## Docker Volume Commands

| Command | Example | Description |
|---------|---------|-------------|
| `docker volume create VOLUME_NAME` | `docker volume create mydata` | Creates a new Docker volume |
| `docker volume ls` | `docker volume ls` | Lists all Docker volumes |
| `docker volume inspect VOLUME_NAME` | `docker volume inspect mydata` | Shows detailed info about a volume |
| `docker volume rm VOLUME_NAME` | `docker volume rm mydata` | Removes a volume |
| `docker run -v VOLUME_NAME:/path/in/container IMAGE` | `docker run -v mydata:/app/data my-app` | Mounts a volume inside a container |

## Docker Network Commands

| Command | Example | Description |
|---------|---------|-------------|
| `docker network ls` | `docker network ls` | Lists all Docker networks |
| `docker network create NETWORK_NAME` | `docker network create mynetwork` | Creates a new user-defined network |
| `docker network inspect NETWORK_NAME` | `docker network inspect mynetwork` | Displays detailed info about a network |
| `docker network rm NETWORK_NAME` | `docker network rm mynetwork` | Deletes a user-defined network |
| `docker run --network NETWORK_NAME IMAGE` | `docker run --network mynetwork my-app` | Connects a container to a specific network |

## Docker Compose Commands

| Command | Example | Description |
|---------|---------|-------------|
| `docker-compose up` | `docker-compose up` | Starts and runs containers defined in `docker-compose.yml` |
| `docker-compose up --build` | `docker-compose up --build` | Builds images before starting the containers |
| `docker-compose down` | `docker-compose down` | Stops and removes containers, networks, volumes defined in the file |
| `docker-compose stop` | `docker-compose stop` | Stops services without removing them |
| `docker-compose start` | `docker-compose start` | Starts existing containers |
| `docker-compose ps` | `docker-compose ps` | Lists containers managed by Compose |
| `docker-compose logs` | `docker-compose logs` | Displays logs for services |
| `docker-compose logs -f` | `docker-compose logs -f` | Follows live logs like `tail -f` |
| `docker-compose exec SERVICE sh` | `docker-compose exec web sh` | Opens a shell inside a running container |
| `docker-compose build` | `docker-compose build` | Manually builds images for services |

### ✅ Run a Single Service with Docker Compose

| Command | Example | Description |
|---------|---------|-------------|
| `docker-compose up SERVICE_NAME` | `docker-compose up vite-app` | Runs a single service from the Compose file |
| `docker-compose up -d SERVICE_NAME` | `docker-compose up -d vite-app` | Runs a single service in detached mode |
| `docker-compose stop SERVICE_NAME` | `docker-compose stop vite-app` | Stops a specific service |
| `docker-compose start SERVICE_NAME` | `docker-compose start vite-app` | Starts a specific stopped service |
| `docker-compose logs SERVICE_NAME` | `docker-compose logs vite-app` | Shows logs for a specific service |
| `docker-compose exec SERVICE_NAME sh` | `docker-compose exec vite-app sh` | Open shell inside a specific service |
