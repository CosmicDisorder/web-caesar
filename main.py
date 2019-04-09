from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 1.25em;
                margin: 0 auto;
                width: 33.75em;
                font: 1em sans-serif;
            }
            textarea {
                margin: .625em;
                width: 33.75em;
                height: 7.5em;
            }
        </style>
    </head>
    <body>
        <h1>I can has form</h1>
        <br> 
        <form method="POST">
        <label> Rotate by: 
            <input name="rotate_x" type="text" value="{rotate_x} />
        </label>
        <label> 
            <input name="rotate_text" type="text" value="{rotate_text} />
        </label>

    </body>
<html>
"""
@app.route("/")
def index():
    return form

app.run()