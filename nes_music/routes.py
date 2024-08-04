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
    Game_alias = aliased(Game, name="Game_alias")

    table = db.session.execute(
        select(Game, Game_alias, Song, SongMusician, Musician, Company, Video)
        .outerjoin(Game, Company.id == Game.developer_id)
        .outerjoin(Game_alias, Company.id == Game_alias.publisher_id)
        .filter(
            Song.game_id == Game.id,
            SongMusician.song_id == Song.id,
            Musician.id == SongMusician.composer_id,
            Game.developer_id == Game.developer_id,
            Game.publisher_id == Game.publisher_id,
            Video.song_id == Song.id
        )
        .order_by(Video.upload_date.desc())
    ).all()

    for t in table:
        print(t.Game.name, t. Song.name, t.Game.developer.name, t.Game.publisher.name)

    return render_template("index.html", table=table)
