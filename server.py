from flask import Flask
from flask import send_from_directory

import os, random
app = Flask(__name__)

# Serving the index file
@app.route('/', methods=['GET'])
def index():
  return generate_html('Random Card')


def generate_html(title):
    bob = True
    return f'''
    <html>
    <head>
        <title>{title}</title>
        <link rel="stylesheet" type="text/css" href="styles.css">
    </head>
    <body>
        <style>{generate_styles()}</style>
        <div class="centered">
            <div id="theCard" class="card suit-hearts">
            <p id="cardContent">A</p>
            </div>
        </div>
        <script type="text/javascript" src="script.js"></script>
    </body>
    </html>
    '''

def generate_styles():
    return r'''
        @charset "UTF-8";
        body {
        background: green;
        }
        .centered{margin-left: auto;margin-right: auto; width: 300px;}
        a.button {
        display: block;
        width: 300px;
        height: 50px;
        background: SandyBrown;
        font-family: Arial;
        text-decoration: none;
        font-size: 25px;
        line-height: 50px;
        text-align: center;
        color: #444;
        font-weight: bold;
        border-radius: 5px;
        box-shadow: 3px 3px 7px rgba(0, 0, 0, 0.3);
        margin-top: 20px;

        }
        a.button:hover {
        background: #f7bf90;
        }

        .card {
        width: 300px;
        height: 440px;
        border-radius: 15px;
        background: white;
        box-shadow: 3px 3px 7px rgba(0, 0, 0, 0.3);
        position: relative;
        }
        .card p {
        font: 150px/440px Times New Roman, serif;
        text-align: center;
        }

        div.suit-hearts:before {
        content: "♥";
        font-size: 90px;
        position: absolute;
        top: 10px;
        left: 10px;
        color: red;
        }

        div.suit-hearts:after {
        content: "♥";
        font-size: 90px;
        position: absolute;
        bottom: 10px;
        right: 10px;
        color: red;
        transform: rotate(180deg);
        }

        div.suit-diamonds:before {
        content: "♦";
        font-size: 90px;
        position: absolute;
        top: 10px;
        left: 10px;
        color: red;
        }

        div.suit-diamonds:after {
        content: "♦";
        font-size: 90px;
        position: absolute;
        bottom: 10px;
        right: 10px;
        color: red;
        transform: rotate(180deg);
        }

        div.suit-spades:before {
        content: "♠";
        font-size: 90px;
        position: absolute;
        top: 10px;
        left: 10px;
        color: black;
        }

        div.suit-spades:after {
        content: "♠";
        font-size: 90px;
        position: absolute;
        bottom: 10px;
        right: 10px;
        color: black;
        transform: rotate(180deg);
        }

        div.suit-clubs:before {
        content: "♣";
        font-size: 90px;
        position: absolute;
        top: 10px;
        left: 10px;
        color: black;
        }

        div.suit-clubs:after {
        content: "♣";
        font-size: 90px;
        position: absolute;
        bottom: 10px;
        right: 10px;
        color: black;
        transform: rotate(180deg);
        }
    '''

app.run(host='0.0.0.0',port=3000, debug=False)
