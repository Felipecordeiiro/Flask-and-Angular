from flask import Flask, render_template, make_response, jsonify, request
from bd import id_task

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/task", me=['GET'])
def task():
    return make_response(
        jsonify(id_task)
        )

@app.route("/task", me=['POST'])
def create_task():
    task = task.json
    id_task.append(task)
    return task

app.run()