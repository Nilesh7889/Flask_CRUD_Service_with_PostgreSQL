class Config:
    # PostgreSQL database URI
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:7889@localhost/authorization_service'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Secret key for session management
    SECRET_KEY = 'nilesh785'