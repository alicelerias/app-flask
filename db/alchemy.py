from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def get_db():
    return db


def configure(app):
    db = get_db()
    db.init_app(app)
    
    app.db = db
