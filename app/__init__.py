from flask import (
    Flask,
    render_template,
)
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import func


app = Flask(__name__, static_folder='../static')
app.config.from_object('config')

db = SQLAlchemy(app)


def _get_page_config():
    class Config(object):
        pass

    config = Config()
    config.title = 'Home'
    config.bootswatch_template = app.config.get('BOOTSWATCH_TEMPLATE')

    return config


@app.route('/')
def index_page():

    posts = Post.query.all()

    return render_template('index.html',
                           posts=posts,
                           config=_get_page_config())


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.TIMESTAMP, server_default=func.now())
    updated = db.Column(db.TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    body = db.Column(db.String(63))

    def __repr__(self):
        return '<Created %s: Body %s>' % (self.created, self.body)
