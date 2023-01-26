from .base import db
from .Project import Project

class Shift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), db.ForeignKey('users.username', ondelete='CASCADE'))
    project_id = db.Column(db.String(), db.ForeignKey('project.name', ondelete='CASCADE'))
    status = db.Column(db.String(), nullable=False)

    def __init__(self, username, project_id, status):
        self.username = username
        self.project_id = project_id
        self.status = status

    def __repr__(self):
        return f'Shift <username:{self.username}, project id:{self.project_id}, status:{self.status}>'

    def as_dict(self):
        return {
            "username": self.username,
            "project_id": self.project_id,
            "status": self.status
        }

    def getId(self):
        return self.id

    def getUsername(self):
        return self.username

    def getProjectId(self):
        return self.project_id

    def getStatus(self):
        return self.status

    def setId(self):
        self.id = id

    def setUsername(self, username):
        self.username = username

    def setProjectId(self, project_id):
        self.project_id = project_id

    def setStatus(self, status):
        self.status = status
    
    @staticmethod
    def getAllVolunteers(projectId):
        return db.session.execute(db.select(Shift).filter_by(Shift.username == projectId))
    
    @staticmethod
    def getAllProjects(user_id):
        return db.session.execute(db.select(Shift).filter_by(Shift.username == user_id))
    
    @staticmethod
    def getPastProjects(user_id):
        return db.session.execute(db.select(Shift).filter_by(Shift.username == user_id, Shift.getStatus() =='Past'))
    
    @staticmethod
    def getUpcomingProjects(user_id):
        return db.session.execute(db.select(Shift).filter_by(Shift.username == user_id, Shift.getStatus()=='Pending'))

    @staticmethod
    def getAllShifts(username):
        import json
        temp = db.session.execute(db.select(Project).join(Shift, Shift.project_id == Project.name).add_columns(Shift.username, Shift.status)).all()
        print(temp[0], isinstance(temp[0], Shift), isinstance(temp[0], Project))
        return json.dumps([i[0].as_dict() for i in temp], indent=4, default=str)


    @staticmethod
    def getPaginatedShifts(username, page):
        temp = db.select(Project).join(Shift, Shift.project_id == Project.name).add_columns(Shift.username, Shift.status)
        res = db.paginate(temp.filter(Shift.username == username).order_by(Project.eventTime), per_page=15, page=int(page))
        return [i.as_dict() for i in res]

    @staticmethod
    def totalPages(user_id):
        temp = db.select(Shift).join(Project, Shift.project_id == Project.name).add_columns(Shift.username, Shift.status)
        res = db.paginate(temp.filter(Shift.username == user_id), per_page=15).pages
        print(f"total pages : {res}")
        return res