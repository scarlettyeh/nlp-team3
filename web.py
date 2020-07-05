from flask import Flask

# create Flask app
app = Flask(__name__)

# create route for /
@app.route('/')

# create index function
def index():
  return 'hello world!'
