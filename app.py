from flask import Flask

#Create a New Flask App Instance
app = Flask(__name__)

#creat routs
@app.route('/')
def hello_world():
    return 'Hello world'