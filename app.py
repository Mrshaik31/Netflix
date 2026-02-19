from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your_default_secret_key')

# Database Configuration
MONGO_URI = os.getenv('MONGO_URI')
TMDB_API_KEY = os.getenv('TMDB_API_KEY')

# Initialize MongoDB Client
try:
    client = MongoClient(MONGO_URI)
    db = client.get_database('netflix_db') # Connect to (or create) the database
    users_collection = db.users # Connect to (or create) the collection
    # Test connection
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('movies'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']

        # Check if user already exists
        if users_collection.find_one({'$or': [{'username': username}, {'email': email}]}):
            flash('Username or Email already exists!')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)

        new_user = {
            'username': username,
            'email': email,
            'password': hashed_password,
            'phone': phone
        }

        try:
            users_collection.insert_one(new_user)
            flash('Registration successful! Please login.')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'Error registering user: {e}')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users_collection.find_one({'username': username})

        if user and check_password_hash(user['password'], password):
            session['user_id'] = str(user['_id'])
            session['username'] = user['username']
            return redirect(url_for('movies'))
        else:
            flash('Invalid username or password')

    return render_template('login.html')

@app.route('/movies')
def movies():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Fetch trending movies from TMDB
    movies_data = []
    if TMDB_API_KEY:
        url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={TMDB_API_KEY}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                movies_data = response.json().get('results', [])
            else:
                 print(f"Error fetching movies: {response.status_code}")
        except Exception as e:
            print(f"Request failed: {e}")
    else:
        print("TMDB_API_KEY is missing.")

    return render_template('movies.html', movies=movies_data)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
