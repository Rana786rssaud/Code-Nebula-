from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'skillswap_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skillswap.db'
db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

# Skill Model
class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    skill_name = db.Column(db.String(80), nullable=False)
    skill_type = db.Column(db.String(10), nullable=False) # 'offer' or 'request'

# Routes
@app.route('/')
def home():
    if 'user_id' in session:
        skills = Skill.query.all()
        return render_template('home.html', skills=skills)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            return 'User already exists!'
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('home'))
        return 'Invalid credentials'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/add_skill', methods=['GET', 'POST'])
def add_skill():
    if request.method == 'POST':
        skill_name = request.form['skill_name']
        skill_type = request.form['skill_type']
        user_id = session['user_id']
        new_skill = Skill(skill_name=skill_name, skill_type=skill_type, user_id=user_id)
        db.session.add(new_skill)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_skill.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
