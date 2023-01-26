from faker import Faker
import random
fake = Faker()



def UserGenerator(count):
    from .models.Users import Users
    from .models.base import db
    from werkzeug.security import generate_password_hash
    names = [fake.unique.name() for _ in range(count)]
    email = [fake.unique.email() for _ in range(count)]
    password = "123"
    user_data = [Users(names[i], email[i], generate_password_hash(password)) for i in range(count)]
    # db.session.add(user_data)
    for user in user_data: db.session.add(user)
    # for i in range(count):
    #     db.session.add(Users(names[i], email[i], generate_password_hash(password)))
    db.session.commit()
    return user_data

def ProjectGenerator(count, users):
    from .models.base import db
    from .models.Project import Project
    from .models.Users import Users
    from datetime import timedelta
    projects = []
    for i in range(count):
        name = fake.company()
        location = fake.address()
        manager = random.choice(users).getUsername()
        published = fake.date_time_this_month()
        eventTime = fake.date_time_this_month(after_now=True)
        endTime = (eventTime + timedelta(hours=random.randint(0,6)))
        project = Project(name, location, manager, published, eventTime, endTime)
        projects.append(project)
        db.session.add(project)
    db.session.commit()

    return projects





def ConnectionsGenerator(count, users):
    from .models.Connections import Connections
    from .models.base import db
    for i in range(count):
        user1, user2 = random.choice(users).getUsername(), random.choice(users).getUsername()
        if user1 != user2:
            db.session.add(Connections(user1, user2))

    db.session.commit()


def ShiftGenerator(count, users, projects):
    from .models.base import db
    from .models.Users import Users
    from .models.Project import Project
    from .models.Shift import Shift
    statuses = ['pending', 'completed']

    for i in range(count):
        user = random.choice(users).getUsername()
        project = random.choice(projects).getName()
        status = random.choice(statuses)
        # print(user, project, status)
        db.session.add(Shift(user, project, status))
    db.session.commit()



def LikesGenerator(count, users, projects):
    from .models.base import db
    from .models.Likes import Likes
    from .models.Users import Users
    from .models.Project import Project

    for i in range(count):
        user = random.choice(users).getUsername()
        project = random.choice(projects).getName()
        db.session.add(Likes(user, project))
    db.session.commit()
        


def DataGenerator(userCount, projectCount, connectionCount, shiftCount, likeCount):
    print('yee')
    users = UserGenerator(userCount)
    projects = ProjectGenerator(projectCount, users)
    ConnectionsGenerator(connectionCount, users)
    ShiftGenerator(shiftCount, users, projects)
    LikesGenerator(likeCount, users, projects)
    ConnectionsGenerator(connectionCount, users)



