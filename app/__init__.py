from flask import Flask, _app_ctx_stack
from sqlalchemy.orm import scoped_session

app = Flask(__name__)

from app import routes
