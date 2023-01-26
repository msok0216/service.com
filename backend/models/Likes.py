from .base import db
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import ARRAY


class Likes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(40), db.ForeignKey('users.username', ondelete='CASCADE'))
    project = db.Column(db.String(40), db.ForeignKey('project.name', ondelete='CASCADE'))


    def __repr__(self):
        return f"Likes<user:{self.user}, project:{self.project}>"

    def __init__(self, user, project):
        self.user = user
        self.project = project

    def as_dict(self):
        return {
            "user": self.user,
            "project": self.project
        }

    
    @staticmethod
    def getUsersAllLikes(user):
        return db.session.execute(db.select(Likes).filter(Likes.user == user))

    @staticmethod
    def getProjectsAllLikes(project):
        return db.session.execute(db.select(Likes).filter(Likes.project == project))