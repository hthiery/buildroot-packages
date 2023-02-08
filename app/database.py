# https://towardsdatascience.com/use-flask-and-sqlalchemy-not-flask-sqlalchemy-5a64fafe22a4

from os.path import isfile
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

SQLALCHEMY_DATABASE_URL = 'sqlite:///br-pkg.db'

Base = declarative_base()


def get_session_db(branch):
    db_filename = 'databases/{}.db'.format(branch)

    if not isfile(db_filename):
        raise FileNotFoundError(db_filename)

    engine = create_engine('sqlite:///{}'.format(db_filename))
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return scoped_session(SessionLocal)
