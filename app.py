from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/mla')
def mla():
    return render_template('MLA.html')
@app.route('/apa')
def apa():
    return render_template('apa.html')

@app.route('/chicago')
def chicago():
    return render_template('chicago.html')