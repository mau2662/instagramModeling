from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
   

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class UserPhotos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
  

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "photo": self.photo,
            "description": self.description,
            # do not serialize the password, its a security breach
        }

class UserVideos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
  

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "video": self.video,
            "description": self.description,
            # do not serialize the password, its a security breach
        }        

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(120), unique=False, nullable=False)
    followers = db.Column(db.Integer, unique=False, nullable=False)
    following = db.Column(db.Integer, unique=False, nullable=False)
    photos= Column(String(250),ForeignKey('UserPhotos.photo'))
    videos= Column(String(250),ForeignKey('UserVideos.video'))

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            "followers": self.followers,
            "following": self.following,
            
            # do not serialize the password, its a security breach
        }        