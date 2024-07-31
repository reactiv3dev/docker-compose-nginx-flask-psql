import os, datetime
from flask import Flask, request

app = Flask(__name__)

@app.route('/about', methods=['GET'] )
def about():
    version=os.environ.get('APP_VERSION')
    env=os.environ.get('ENV')

    return { "version": version, "environment": env }, 200

@app.route('/secrets', methods=['GET'])
def secrets():
    creds: dict = dict()
    creds['DB_USER']: str = os.environ.get('DB_USER')
    creds['DB_PASSWORD']: str = os.environ.get('DB_PASSWORD')
    #next will  be null for example
    creds['UNKNOWN_VAR']: str = os.environ.get('UNKNOWN_VAR') 
    #next will be in compose.yaml as required
    creds['APP_TOKEN']: str = os.environ.get('APP_TOKEN')
    return creds, 200

@app.route('/log_transactions', methods=['GET', 'POST'])
def log_transactions():
    filename = '/data/transaction_logs.txt'

    if(request.method == 'POST'):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as f:
            f.write(f'Customer log ----- {datetime.datetime.now()}')
        return { "success": True }, 201
    
    if(request.method == 'GET'):
        f = open(filename, 'r')
        logs = f.read()
        f.close()

        return { "logs": logs }, 200