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
        return (f"<id = {self.id},"
                f"name = {self.name}")


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    game_id = db.Column(db.Integer, db.ForeignKey("game.id"))
    composer_id = db.Column(db.Integer, db.ForeignKey("composer.id"))
    arranger_id = db.Column(db.Integer, db.ForeignKey("arranger.id"))

    game = db.relationship("Game", back_populates="song")
    composer = db.relationship("Composer", back_populates="song")
    arranger = db.relationship("Arranger", back_populates="song")

    def __repr__(self):
        return (f"<id = {self.id},"
                f"name = {self.name},"
                f"game_id = {self.game_id},"
                f"game = {self.game.name}")


class Composer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    song = db.relationship("Song", back_populates="composer")

    def __repr__(self):
        return (f"<id = {self.id},"
                f"name = {self.name}")


class Arranger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    song = db.relationship("Song", back_populates="arranger")

    def __repr__(self):
        return (f"<id = {self.id},"
                f"name = {self.name}")


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
        return (f"<id = {self.id},"
                f"name = {self.name}")

    # Info re relationship to same table using multiple FKs:
    # https://stackoverflow.com/questions/65941555/sqlalchemy-error-multiple-foreign-keys-references-to-the-same-table-and-column/65994756#65994756



class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game = db.Column(db.String)
    song = db.Column(db.String)
    composer = db.Column(db.String)
    add_personnel = db.Column(db.String)
    developer = db.Column(db.String)
    publisher = db.Column(db.String)
    year = db.Column(db.String)
    description = db.Column(db.String)
    more_info = db.Column(db.String)
    date_uploaded = db.Column(db.DateTime)
    link = db.Column(db.String)
    process_note = db.Column(db.String)

    def __repr__(self):
        return (f"<id = {self.id},"
                f"game = {self.game},"
                f"song = {self.song}>")
