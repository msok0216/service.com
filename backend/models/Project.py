from .base import db
from sqlalchemy import select

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    location = db.Column(db.String())
    manager = db.Column(db.String(), db.ForeignKey('users.username', ondelete='CASCADE'))
    published = db.Column(db.DateTime(), nullable=False)
    eventTime = db.Column(db.DateTime(), nullable=False)
    endTime = db.Column(db.DateTime())

    def __repr__(self):
        return (
            f'Project <id:{self.id}, name:{self.name}, manager:{self.manager}, location:{self.location}'
            f'published:{self.published}, eventTime:{self.eventTime}, endTime:{self.endTime}>'
        )

    def __init__(self, name, location, manager, published, eventTime, endTime):
        self.name = name
        self.location = location
        self.manager = manager
        self.published = published
        self.eventTime = eventTime
        self.endTime = endTime

    def as_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "manager": self.manager,
            "published": self.published,
            "eventTime" : self.eventTime,
            "endTime": self.endTime
        }

    def edit(self, name, location, manager, published, eventTime, endTime):
        self.name = name
        self.location = location
        self.manager = manager
        self.published = published
        self.eventTime = eventTime
        self.endTime = endTime

    @staticmethod
    def getProjects(name=None, location=None, manager=None):
        return db.session.execute(db.select(Project).filter_by(name == Project.name | manager == Project.manager | location == Project.location))

    @staticmethod
    def getPaginatedProjects(name=None, location=None, manager=None):
        results = db.paginate(db.select(Project).order_by(Project.published))
        return  results

    def getName(self):
        return self.name

    def getLocation(self):
        return self.location
    
    def getManager(self):
        return self.manager
    
    def getPublished(self):
        return self.published
    
    def getEventTime(self):
        return self.eventTime
    
    def getEndTime(self):
        return self.endTime






    


    


