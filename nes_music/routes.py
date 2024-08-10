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
        select(Game, Song, Video)
        .filter(Song.game_id == Game.id,
                Video.song_id == Song.id)
        .order_by(Video.upload_date.desc())
        ).all()

    all_composers, all_arrangers = get_all_musicians()

    return render_template("index.html",
                           table=table,
                           composers=all_composers,
                           arrangers=all_arrangers)


@app.route("/songs_alphabetically")
def songs_alphabetically():
    table = db.session.execute(
        select(Game, Song, Video)
        .filter(Song.game_id == Game.id,
                Video.song_id == Song.id)
        .order_by(Game.name, Video.upload_date.desc())
        ).all()

    all_composers, all_arrangers = get_all_musicians()

    return render_template("songs_alphabetically.html",
                           table=table,
                           composers=all_composers,
                           arrangers=all_arrangers)


def get_all_musicians():
    song_query = db.session.execute(select(Song))

    song_ids = [0]  # 0 added here allows list index to match Song.id
    for song_id in song_query:
        song_ids.append(song_id.Song.id)  # Creates list of desc ids

    all_composers = []
    all_arrangers = []
    for song_id in song_ids:
        songs = db.session.execute(
            select(SongMusician)
            .filter(SongMusician.song_id == Song.id,
                    Song.id == song_id)
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

    return all_composers, all_arrangers
