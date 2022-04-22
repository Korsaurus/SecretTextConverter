from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from converter import Converter
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField

c = Converter()


class ConvertToMorseForm(FlaskForm):
    input = StringField("Message", validators=[DataRequired()])
    submit = SubmitField("Convert")


class ConvertFromMorseForm(FlaskForm):
    input = StringField("Morse Code", validators=[DataRequired()])
    submit = SubmitField("Convert")


app = Flask(__name__)
# TODO - app.config['SECRET_KEY'] = ''
Bootstrap(app)

@app.route("/")
def home():

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
