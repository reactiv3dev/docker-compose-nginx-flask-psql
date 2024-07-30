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
docker run -p 7070:8080 reactiv3dev/flask:0.1.0
```