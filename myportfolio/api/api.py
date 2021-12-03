import time
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time' : time.time()}

if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run('localhost', debug=False)