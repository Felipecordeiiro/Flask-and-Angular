from flask import Flask, render_template, make_response, jsonify
from bd import id_task

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/task", me=['GET'])
def api():
    return make_response(
        jsonify(id_task)
        )

app.run()