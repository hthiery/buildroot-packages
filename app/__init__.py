from flask import Flask, _app_ctx_stack
from sqlalchemy.orm import scoped_session

from .database import SessionLocal, engine

app = Flask(__name__)
app.session = scoped_session(SessionLocal)

from app import routes
