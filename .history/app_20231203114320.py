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

def create_task():


if __name__ == "__main__": 
    app.run(debug=True)