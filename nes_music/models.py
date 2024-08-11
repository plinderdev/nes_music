from nes_music import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    developer_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    publisher_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    year = db.Column(db.Integer)

    song = db.relationship("Song", back_populates="game")
    developer = db.relationship("Company",
                                foreign_keys=[developer_id],
                                back_populates="as_dev")
    publisher = db.relationship("Company",
                                foreign_keys=[publisher_id],
                                back_populates="as_pub")

    def __repr__(self):
        return (f"<id = {self.id}, "
                f"name = {self.name}>")


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    game_id = db.Column(db.Integer, db.ForeignKey("game.id"))

    game = db.relationship("Game", back_populates="song")
    song_musician = db.relationship("SongMusician", back_populates="song")

    def __repr__(self):
        return (f"<id = {self.id}, "
                f"name = {self.name}, "
                f"game_id = {self.game_id}, "
                f"name = {self.game.name}>")


class SongMusician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey("song.id"))
    composer_id = db.Column(db.Integer, db.ForeignKey("musician.id"))
    arranger_id = db.Column(db.Integer, db.ForeignKey("musician.id"))

    song = db.relationship("Song", back_populates="song_musician")
    composer = db.relationship("Musician",
                               foreign_keys=[composer_id],
                               back_populates="as_composer")
    arranger = db.relationship("Musician",
                               foreign_keys=[arranger_id],
                               back_populates="as_arranger")

    def __repr__(self):
        return (f"<id = {self.id}, "
                f"song = {self.song.name}, "
                f"composer = {self.composer}, "
                f"arranger = {self.arranger}>")


class Musician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    as_composer = db.relationship("SongMusician",
                                  foreign_keys=[SongMusician.composer_id],
                                  back_populates="composer")
    as_arranger = db.relationship("SongMusician",
                                  foreign_keys=[SongMusician.arranger_id],
                                  back_populates="arranger")

    def __repr__(self):
        return (f"<id = {self.id}, "
                f"name = {self.name}>")


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    as_dev = db.relationship("Game",
                             foreign_keys=[Game.developer_id],
                             back_populates="developer")
    as_pub = db.relationship("Game",
                             foreign_keys=[Game.publisher_id],
                             back_populates="publisher")

    def __repr__(self):
        return (f"<id = {self.id}, "
                f"name = {self.name}>")

    # Info re relationship to same table using multiple FKs:
    # https://stackoverflow.com/questions/65941555/sqlalchemy-error-multiple-foreign-keys-references-to-the-same-table-and-column/65994756#65994756


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("game.id"))
    song_id = db.Column(db.Integer, db.ForeignKey("song.id"))
    description = db.Column(db.String)  # YouTube first sentence
    desc_note = db.Column(db.String)  # YouTube any additional note
    process_note = db.Column(db.String)  # My note on video creation
    upload_date = db.Column(db.DateTime)
    link = db.Column(db.String)

    playlist_video = db.relationship("PlaylistVideo", back_populates="video")

    def __repr__(self):
        return (f"<id = {self.id}, "
                f"game = {self.game_id}, "
                f"song = {self.song_id}, "
                f"link = {self.link}>")


class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    link = db.Column(db.String)

    playlist_video = db.relationship("PlaylistVideo",
                                     back_populates="playlist")

    def __repr__(self):
        return (f"<id = {self.id}, "
                f"name = {self.game}, "
                f"link = {self.link}>")


class PlaylistVideo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlist.id"))
    video_id = db.Column(db.Integer, db.ForeignKey("video.id"))

    playlist = db.relationship("Playlist", back_populates="playlist_video")
    video = db.relationship("Video", back_populates="playlist_video")

    def __repr__(self):
        return (f"<id = {self.id}, "
                f"playlist = {self.playlist.name}, "
                f"video = {self.video.song_id}>")
