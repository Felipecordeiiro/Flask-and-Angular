from flask import Flask, render_template, make_response, jsonify, request
from bd import id_task

app = Flask(__name__)
app.json.sort_keys = False


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/task", methods=['GET'])
def task():
    return make_response(
        jsonify(
            message = 'Lista de task',
            dados = id_task
            )
        )

@app.route("/task", methods=['POST'])
def create_task():
    task = request.json
    id_task.append(dict(task))
    return make_response(
        jsonify(
            message = 'Task adicionada com sucesso!',
            dados = task
            )
        )

if __name__ == "__main__": 
    app.run(debug=True)