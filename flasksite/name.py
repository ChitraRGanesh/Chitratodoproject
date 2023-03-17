from flask import Flask
name=Flask(__name__)


# @name.route('/profile/<username>')
# def home(username):
#     return '<h1>This profile is for %s </h1>' % username

@name.route('/profile/<int:id>')
def home(id):
    return '<h1>This profile is for %d </h1>' % id

name.run()