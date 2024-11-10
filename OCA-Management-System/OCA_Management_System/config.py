import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "mysql+pymysql://root:1234@localhost:3306/oca_management_system")
    SQLALCHEMY_TRACK_MODIFICATIONS = True