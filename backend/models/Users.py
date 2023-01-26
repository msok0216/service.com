from .base import db
from sqlalchemy import select
# from sqlalchemy.dialects.postgresql import ARRAY
from .Shift import Shift
from .Likes import Likes
from .Connections import Connections

class Users(db.Model):
    username = db.Column(db.String(40), primary_key=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    # friends = db.Column(ARRAY(db.String(), dimensions=1), db.ForeignKey("users.username"))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User <username:{self.username}, email:{self.email}, password:{self.password}>"
    
    def as_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }

    @staticmethod
    def getProjects(user_id):
        return Shift.getAllProjects(user_id)

    @staticmethod
    def getPastProjects(user_id):
        return Shift.getPastProjects(user_id)

    @staticmethod
    def getUpcomingProjects(user_id):
        return Shift.getUpcomingProjects(user_id)

    @staticmethod
    def getUser(username):
        # print(len(db.session.execute(db.select(User).filter(User.username == username))))
        return db.session.execute(db.select(Users).filter((Users.username == username )| (Users.email == username))).first()

    def getUsername(self):
        return self.username

    def getEmail(self):
        return self.email
    
    def getPassword(self):
        return self.password

    def setUsername(self, username):
        self.username = username

    def setEmail(self, email):
        self.email = email
    
    def setPassWord(self, password):
        self.password = password

