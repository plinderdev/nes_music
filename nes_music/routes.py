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


@app.route("/game")
def game():
    table = db.session.execute(
            select(Game, Song, Video)
            .filter(Song.game_id == Game.id,
                    Video.song_id == Song.id)
            .order_by(Game.name, Video.upload_date.desc())
            ).all()

    all_composers, all_arrangers = get_all_musicians()

    game_first_letters = []
    for row in table:
        if row.Game.name[0] not in game_first_letters:
            game_first_letters.append(row.Game.name[0])

    return render_template("game.html",
                           table=table,
                           composers=all_composers,
                           arrangers=all_arrangers,
                           game_first_letters=game_first_letters)


@app.route("/company")
def company():
    companies = db.session.execute(
                select(Company)
                .order_by(Company.name)
                ).all()
    # for c in companies:
        # print(c.Company.name)

    company_ids = []
    for c in companies:
        company_ids.append(c.Company.id)
    # print(company_ids)

    companies_list = []
    for company_id in company_ids:
        developer = db.session.execute(
                    select(Game, Song, Video)
                    .filter(Song.game_id == Game.id,
                            Video.song_id == Song.id,
                            Game.developer_id == company_id)
                    ).all()
        if developer:
            companies_list.append(developer)
    # print(developers)
    #
    # publishers = []
    # for company_id in company_ids:
        publisher = db.session.execute(
                    select(Game, Song, Video)
                    .filter(Song.game_id == Game.id,
                            Video.song_id == Song.id,
                            Game.publisher_id == company_id)
                    ).all()
        if publisher:
            companies_list.append(publisher)
    # print(publishers)

    new_companies_list = []
    for company in companies_list:
        for row in company:
            if row not in new_companies_list:
            # if row.Game.developer_id == row.Game.publisher_id:
            #     if row not in new_companies_list:
                new_companies_list.append(row)
            # else:
            #     new_companies_list.append(row)
                print(row)

    # for row in new_companies_list:
    #     print(row.Game.name)

    all_composers, all_arrangers = get_all_musicians()

    letters = db.session.execute(
            select(Game, Song, Video)
            .filter(Song.game_id == Game.id,
                    Video.song_id == Song.id)
            ).all()
    company_first_letters = []
    for row in letters:
        if row.Game.developer.name[0] or row.Game.publisher.name[0] not in company_first_letters:
            company_first_letters.append(row.Game.developer.name[0])
            company_first_letters.append(row.Game.publisher.name[0])

    return render_template("company.html",
                           companies=companies,
                           table=new_companies_list,
                           composers=all_composers,
                           arrangers=all_arrangers,
                           company_first_letters=company_first_letters)



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
