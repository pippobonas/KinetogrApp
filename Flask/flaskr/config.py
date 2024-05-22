class Config:
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///KinetogrApp.db?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False