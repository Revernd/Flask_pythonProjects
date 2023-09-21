from flask import Flask
from helloapp.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
print(Config.SQLALCHEMY_DATABASE_URI)
migrate = Migrate(app, db)
from helloapp import routes, models


if __name__ == '__main__':
    app.run()

