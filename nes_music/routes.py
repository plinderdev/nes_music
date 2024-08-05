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

    ids = []
    for s in song_ids_query:
        ids.append(s.Song.id)

    all_composers = []
    for id in ids:
        songs = db.session.execute(
            select(SongMusician)
            .filter(SongMusician.song_id == Song.id,
                    Song.id == id)
            .order_by(Song.id.desc())
            )

        song_composers = []
        for s in songs:
            if s.SongMusician.composer:
                song_composers.append(s.SongMusician.composer.name)

        all_composers.append(song_composers)

    print(all_composers)





    table = db.session.execute(
            select(Game, Song, Video) # SongMusician,
            # .outerjoin(Musician, SongMusician.composer_id == Musician.as_composer)
            .filter(
                Song.game_id == Game.id,
                # SongMusician.song_id == Song.id,
                Video.song_id == Song.id
                )
            .order_by(Video.upload_date.desc())
            ).all()



    # for s in songs:
    #     if s.SongMusician.composer:
    #         print(s.Song.id, s.SongMusician.composer.name)

    return render_template("index.html", table=table, composers=all_composers)
