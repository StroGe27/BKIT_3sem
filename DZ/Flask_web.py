from flask import Flask
from generator import fib
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/fibonachi")
def fibonachi_start():
    return "Write after URL '/number!'"

@app.route("/fibonachi/<int:n>")
def fibonachi_number(n):
    return list(fib(n))

@app.errorhandler(404)
def page_not_found(e):
    return "Oops! Try to enter a '/fibonachi/number!'"
