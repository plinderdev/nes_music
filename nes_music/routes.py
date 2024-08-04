from flask import render_template
from sqlalchemy import select
from sqlalchemy.orm import aliased

from nes_music import app
from nes_music import db
from nes_music.models import (Game, Song, SongMusician, Musician, Company,
                              Video, Playlist, PlaylistVideo)


@app.route("/")
@app.route("/index")
def index():
    table = db.session.execute(
            select(Game, Song, SongMusician, Video)
            .outerjoin(Musician, SongMusician.composer_id == Musician.as_composer)
            .filter(
                Song.game_id == Game.id,
                SongMusician.song_id == Song.id,
                Video.song_id == Song.id
                )
            .order_by(Video.upload_date.desc())
            ).all()

    for t in table:
        if t.SongMusician.composer:
            print(t.SongMusician.composer.name)

    return render_template("index.html", table=table)
