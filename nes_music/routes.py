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
    Company_alias = aliased(Company, name="Company_alias")

    table = db.session.execute(
        select(Game, Company_alias, Song, Company, Video) # SongMusician, Musician,
        .outerjoin(Company, Game.developer_id == Company.as_dev)
        .outerjoin(Company_alias, Game.publisher_id == Company_alias.as_pub)
        .filter(
            Song.game_id == Game.id,
            # SongMusician.song_id == Song.id,
            # Musician.id == SongMusician.composer_id,
            # Game.developer_id == Company.as_dev,
            # Game.publisher_id == Company_alias.as_pub,
            Video.song_id == Song.id
        )
        .order_by(Video.upload_date.desc())
    ).all()

    for t in table:
        print(t.Game.name, t. Song.name, t.Game.developer.name, t.Game.publisher.name)

    return render_template("index.html", table=table)
