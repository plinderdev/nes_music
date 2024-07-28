from flask import render_template
from sqlalchemy import select

from nes_music import app
from nes_music import db
from nes_music.models import Video


@app.route("/")
@app.route("/index")
def index():
    table = db.session.execute(select(Video)).all()

    return render_template("index.html", table=table)
