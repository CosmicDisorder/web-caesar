from flask import Flask, request, redirect, render_template
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('form.html'.format())

@app.route("/", methods=['POST'])
def caesar_encrypt():
    text=request.form['text']
    rot=int(request.form['rot'])
    test_text="this is a test"
    new_text=encrypt(text,rot)
    return render_template('form.html', new_text=new_text)

app.run()
