from flask import Flask
app=Flask(__name__)


@app.route('/')
def home():
    return '<h1>Hello World</h1>'
@app.route(('/new'))
def new():
    return '<h1>Hi am New</h1>'
app.run()