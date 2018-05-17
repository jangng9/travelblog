from flask import Flask, render_template
import os

app = Flask(__name__)
app.debug = True
import travelblog.views

if __name__ == "__main__":
    app.run()
