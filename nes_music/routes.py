from flask import render_template
from sqlalchemy import select, func
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

    composers, arrangers = get_all_musicians()

    count_videos = db.session.execute(db.func.count(Video.id)).scalar()

    return render_template("index.html",
                           table=table,
                           composers=composers,
                           arrangers=arrangers,
                           count_videos=count_videos)


@app.route("/game")
def game():
    table = db.session.execute(
            select(Game, Song, Video)
            .filter(Song.game_id == Game.id,
                    Video.song_id == Song.id)
            .order_by(Game.name, Video.upload_date.desc())
            ).all()

    composers, arrangers = get_all_musicians()

    game_first_letters = []
    for row in table:
        if row.Game.name[0] not in game_first_letters:
            game_first_letters.append(row.Game.name[0])

    count_games = db.session.execute(db.func.count(Game.id)).scalar()

    return render_template("game.html",
                           table=table,
                           composers=composers,
                           arrangers=arrangers,
                           game_first_letters=game_first_letters,
                           count_games=count_games)


@app.route("/company")
def company():
    # Query used to create company_ids list and for comparison at company.html
    companies = db.session.execute(
                select(Company)
                .order_by(Company.name)
                ).all()

    company_ids = []
    for c in companies:
        company_ids.append(c.Company.id)

    # These are the data objects:
    table = []
    for company_id in company_ids:
        developer = db.session.execute(
                    select(Game, Song, Video)
                    .filter(Song.game_id == Game.id,
                            Video.song_id == Song.id,
                            Game.developer_id == company_id)
                    .order_by(Game.name, Video.upload_date.desc())
                    ).all()
        if developer:
            for row in developer:  # This pops each row out of developer list
                if row not in table:
                    table.append(row)

        publisher = db.session.execute(
                    select(Game, Song, Video)
                    .filter(Song.game_id == Game.id,
                            Video.song_id == Song.id,
                            Game.publisher_id == company_id)
                    .order_by(Game.name, Video.upload_date.desc())
                    ).all()
        if publisher:
            for row in publisher:  # This pops each row out of publisher list
                if row not in table:
                    table.append(row)

    composers, arrangers = get_all_musicians()

    company_first_letters = []
    for row in table:
        if row.Game.developer.name[0] not in company_first_letters:
            company_first_letters.append(row.Game.developer.name[0])
        if row.Game.publisher.name[0] not in company_first_letters:
            company_first_letters.append(row.Game.publisher.name[0])

    count_companies = len(company_ids)

    return render_template("company.html",
                           companies=companies,
                           table=table,
                           composers=composers,
                           arrangers=arrangers,
                           company_first_letters=company_first_letters,
                           count_companies=count_companies)

@app.route("/composer")
def composer():
    # Query of all musicians used for comparison and more at composer.html
    musicians = db.session.execute(
                select(Musician)
                .order_by(Musician.last_name)
                ).all()

    # Query for usual table data
    table = db.session.execute(
            select(Game, Song, Video)
            .filter(Song.game_id == Game.id,
                    Video.song_id == Song.id)
            .order_by(Video.upload_date.desc())
            ).all()

    # Used at composer.html for comparison to musicians and to show table data
    composers, arrangers = get_all_musicians()

    musician_first_letters = []
    for row in musicians:
        if row.Musician.last_name[0] not in musician_first_letters:
            musician_first_letters.append(row.Musician.last_name[0])

    def get_count(musician):
        count = 0
        musician_ids = []
        for m in musician:
            for row in m:
                if row.id not in musician_ids:
                    musician_ids.append(row.id)
                    count += 1
        return count

    count_composers = get_count(composers)
    count_arrangers = get_count(arrangers)

    return render_template("composer.html",
                           musicians=musicians,
                           table=table,
                           composers=composers,
                           arrangers=arrangers,
                           musician_first_letters=musician_first_letters,
                           count_composers=count_composers,
                           count_arrangers=count_arrangers)


def get_all_musicians():
    song_query = db.session.execute(select(Song))

    song_ids = [0]  # 0 added here allows list index to match Song.id
    for song_id in song_query:
        song_ids.append(song_id.Song.id)  # Creates list of desc ids

    composers = []
    arrangers = []
    for song_id in song_ids:
        songs = db.session.execute(
            select(SongMusician)
            .filter(SongMusician.song_id == Song.id,
                    Song.id == song_id)
            .order_by(SongMusician.id)  # Entered into db in order I want
        )

        song_composers = []
        song_arrangers = []
        for s in songs:
            if s.SongMusician.composer:
                song_composers.append(s.SongMusician.composer)
            if s.SongMusician.arranger:
                song_arrangers.append(s.SongMusician.arranger)

        composers.append(song_composers)
        arrangers.append(song_arrangers)

    return composers, arrangers
