from flask import Flask, render_template, make_response
from bd import id_task

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/task", methods=['GET'])
def api():
    return id_task

app.run()