from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
import werkzeug
from wtforms import StringField, SubmitField, Label, PasswordField
from wtforms.validators import DataRequired, Length
import requests
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
