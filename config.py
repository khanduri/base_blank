import os
basedir = os.path.abspath(os.path.dirname(__file__))


BOOTSWATCH_TEMPLATE_LIST = ["paper", "sandstone", "cosmo", "darkly", "yeti", "slate", "superhero"]
BOOTSWATCH_TEMPLATE = BOOTSWATCH_TEMPLATE_LIST[5]


SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'app.db'))
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

