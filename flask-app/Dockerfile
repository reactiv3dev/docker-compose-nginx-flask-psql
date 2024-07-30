FROM python:3.12.4-alpine3.20

# We need curl for health check
RUN apk --no-cache add curl

WORKDIR /app

# First, copy dependencies list only
COPY requirements.txt .

# Install dependencires from requirements file
RUN pip install -r requirements.txt

## Copy the app source separately significantly improves
## Build time by using cache if no new depnedencies are added
## This is good for hot-reload while developing
COPY app.py .

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]