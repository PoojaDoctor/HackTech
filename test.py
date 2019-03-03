from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def my_form_post():
    if request.method=='GET':
        return render_template('text.html')
    else:
        text = request.args.get("name", " ")
        print(text)
        return text

if __name__ == "__main__":
	app.run()
