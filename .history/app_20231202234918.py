from flask import Flask, render_template
from bd
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

def api():



app.run()