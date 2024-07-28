from flask import render_template

from nes_music import app
from nes_music import db
from nes_music.models import Video


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")