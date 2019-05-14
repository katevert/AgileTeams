from application import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(128), index=True, unique=False)
    teams = db.Column(db.String(128), index=True, unique=False)
    members = db.Column(db.String(128), index=True, unique=False)
    #images = db.relationship('FileContents', backref = 'register', lazy = True)

    def __init__(self, notes,teams,members):
        self.notes = notes
        self.teams = teams
        self.members = members

    def __repr__(self):
        return '<Data %r, %r, %r>' % self.notes % self.teams % self.members



class FileContents(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)
    #member_id = db.Column(db.Integer, db.ForeignKey('data.id'), nullable = False)
