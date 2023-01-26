import redis
SECRET_KEY='dev'
# DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
SESSION_TYPE = "redis"
SESSION_PERMANENT = False
# PERMANENT_SESSION_LIFETIME = timedelta(days=7),
SESSION_USE_SIGNER=True
SESSION_REDIS = redis.from_url('redis://localhost:6379')
SQLALCHEMY_DATABASE_URI = ("postgresql://service:service@localhost:5432/service")
SQLALCHEMY_TRACK_MODIFICATIONS = False