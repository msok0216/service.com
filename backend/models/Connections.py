from .base import db
from sqlalchemy import select


class Connections(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user1 = db.Column(db.String(40), db.ForeignKey('users.username', ondelete='CASCADE'))
    user2 = db.Column(db.String(40), db.ForeignKey('users.username', ondelete='CASCADE'))


    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2

    def __repr__(self):
        return f"Connections <user1:{self.user1}, user2:{self.user2}>"

    def as_dict(self):
        return {
            "user1": self.user1,
            "user2": self.user2
        }

    @staticmethod
    def getConnections(user):
        connections = db.session.execute(db.select(Connections.user2).filter(Connections.user1 == user)).all()
        # print(connections)
        return [{'user': str(i[0])} for i in connections]
    
    @staticmethod
    def connected(user1, user2):
        connections = db.session.execute(db.select(Connections).filter_by(Connections.user1 == user1 & Connections.user2 == user2))
        return connections is not None

