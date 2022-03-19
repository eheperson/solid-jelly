from flask import Flask
from fask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# app.config['SQL_ALCHEMY_DATABASE'] = 'sqlite:////tmp/test.db'
app.config['SQL_ALCHEMY_DATABASE'] = 'postgresql://postgres_user:postgres_pw@localhost/test_db'

db.init_app(app)
with app.app_context():
    # To create / use database mentioned in URI
    db.create_all()
    db.session.commit()


@app.route('/')
def index():
    return "<h1> enivicivokki </h1>"

if __name__ == '__main__':
    app.run(debug=True)