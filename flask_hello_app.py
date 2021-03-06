from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Juli1984@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<PersonID: {self.id}, PersonName: {self.name}>'


db.create_all()


@app.route('/')
def index():
    person = Person.query.first()
    return f'Hello {person.name}!'


# always include this at the bottom of your code
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
