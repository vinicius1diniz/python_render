from flask import Flask;

app = Flask(__name__)

@app.route('/')
def index():
    return 'BEM VINDO AO MUNDO... DEVOPS.!!! -- Version: 0.3'

@app.route('/msg')
def msg():
    return 'Usando os conceitos de deploy..!!!'

#app.run();