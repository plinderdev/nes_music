from nes_music import db


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
