from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thatIsASecretKey'
# die Adresse für die Datenbank, in dem Fall im Verzeichniss "intance" liegt.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask-admin-tutorial.db'

# db ist die Datenbank
db = SQLAlchemy(app)

# das flask-admin tool
admin = Admin(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(60), nullable=True)


# fügt die Anzeige Model in das Admin-Panel
admin.add_view(ModelView(User, db.session))

with app.app_context():
    # erstellt alle Tabellen für die Datenbank, in dem Fall nur die Tabelle "User"
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
