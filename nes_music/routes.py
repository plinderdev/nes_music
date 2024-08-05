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
    song_ids_query = db.session.execute(
               select(Song)
               .order_by(Song.id) # not desc because appending names below makes it desc
               )

    ids = [0] # put 0 here and I don't need to subtract 1 at html composer td
    for s in song_ids_query:
        ids.append(s.Song.id)

    all_composers = []
    all_arrangers = []
    for id in ids:
        songs = db.session.execute(
            select(SongMusician)
            .filter(SongMusician.song_id == Song.id,
                    Song.id == id)
            .order_by(Song.id.desc())
            )

        song_composers = []
        song_arrangers = []
        for s in songs:
            if s.SongMusician.composer:
                song_composers.append(s.SongMusician.composer.name)
            if s.SongMusician.arranger:
                song_arrangers.append(s.SongMusician.arranger.name)

        all_composers.append(song_composers)
        all_arrangers.append(song_arrangers)

    table = db.session.execute(
            select(Game, Song, Video)
            .filter(
                Song.game_id == Game.id,
                Video.song_id == Song.id
                )
            .order_by(Video.upload_date.desc())
            ).all()

    return render_template("index.html", table=table,
                           composers=all_composers,
                           arrangers=all_arrangers)
