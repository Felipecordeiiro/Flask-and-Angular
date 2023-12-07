from flask import Flask, render_template, make_response, jsonify, request
from bd import id_task

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/task", methods=['GET'])
def task():
    return make_response(
        jsonify(id_task)
        )

@app.route("/task", methods=['POST'])
def create_task():
    task = request.json
    id_task.append(task)
    return make_response(
        task)

if __name__ == "__main__": 
    app.run(debug=True)