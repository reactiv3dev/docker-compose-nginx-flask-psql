# docker-compose-nginx-flask-psql

## Flask-App
1. Make separate directory for flask-app
2. Initialize virtual environment with tool of choice (I used venv):
```
>> python -m venv .venv (.venv is name of the environment)
```
3. Activate newly created environment, with venv it is with command:
```
>> .venv\Scripts\activate
```
4. Install Flask framework as dependency, and any other need dependecy, 
best advice is to choose  and require specific version of package, not the latest one:
```
>> pip install Flask==3.0.3
```
5. To prepare dependencies for later easy install into docker container, we freeze depnedencies into requirements file, as:
```
>> pip freeze > requirements.txt
```
6. Scaffold basic Flask app by instantiating as follows:
```
from flask import Flask

app = Flask(__name__)

@app.route('/about', method=['GET'])
def about():
    version='0.1.0'

    return { "version": version }, 200

```
7. Run it with command:
```
>> flask --app app run
```

8. For running our app in productio we would need wsgi server, so we will install `gunicorn`:
```
>> pip install gunicorn
```

9. Than freeze dependencies in requirements.txt file:
```
>> pip freeze > requirements.txt
```

10. We define `Dockerfile` for the flask app in the directory with given description of `docker image` we wanted.

11. Leave `venv` virtual env by typing:
```
>> deactivate
```

12. Command for conteinerizing image is:
```
docker build -t reactiv3dev/flask:0.1.0 .

docker run -p 7070:8080 reactiv3dev/flask:0.1.0
```


## Docker compose up

1. At the projects root is defined `compose.yaml` file which defines services and has set the instructions on how to build each service by each defined in its own `Dockerfile`, and how to set up Network, Exposed ports, Environement variables etc..
```
docker compose up --build (--build flag in order to rebuild on changes in files)
```


## Pesistence with `Volumes` and `Bind mounts`
- Bind mounts have been arounds since early days of Docker. Bind mounts have limited functionality in compoarison to `volumes`. When you use `bind mount`, a file or directory on host machine is mounted into a container. The file or directory is refrenced by its absolute path on the host machine. By contrast, when we use `volume`, a new directory is created within a Docker's storage direcotry on the host machine, and Docker manages that directory's contents.
* ADVANTAGES OF VOLUMES OVER BIND MOUNTS:
    - Volumes are easier to backup or migrate dthan bind mounts.
    - You can manage volumes using Docker CLI commands or the Docker API
    - Volumes work on both Linux and Windows containers.
    - Volumes acan be more safely shared among multiple containers.
    - Volume drivers let you store volumes on remote hosts or cloud providers,
    encrypt the contents of volumes, or add other functionality.
    - New volumes can have their content pre-populated by a container.
    - Volumes on Docker Desktop have much higher performance than bind mounts from Mac and Windows hosts.

- For`Bind mounts` example we just define volumen dir in our physical place that will reflect onto dir in conteinarized app `./our_dir:./container_dir`:
```
volumes:
    - ./flask-app/my-data:/data
```

- For `Volumes` example, we need to define name on top level of `volumes` and the same name with `:` delimiter against apps containerized dir:
```
services:
    flask-app:
        volumes:
            flask-storage:/data

volumes
    flask-storage:
```