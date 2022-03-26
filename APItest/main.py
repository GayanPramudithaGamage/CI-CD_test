import os
from dotenv import load_dotenv
from flask import (Flask,
                   flash,
                   render_template,
                   redirect,
                   request,
                   url_for)

load_dotenv()
app=Flask(__name__)
app.secret_key="presenze_SSH"

def send_message(to, body):
    # TODO: Send the text message
    pass

@app.route("/")
def message():
    return "hello world"

@app.route("/add-compliment", methods=["POST"])
def add_compliment():
    sender = request.values.get('sender', 'Someone')
    receiver = request.values.get('receiver', 'Someone')
    compliment = request.values.get('compliment', 'wonderful')
    to = request.values.get('to')
    body = f'{sender} says: {receiver} is {compliment}. See more compliments at {request.url_root}'
    send_message(to, body)
    flash('Your message was successfully sent')
    return redirect(url_for('login.html'))

if __name__ == '__main__':
    app.run()