# Netflix Clone - Flask Application (MongoDB Atlas Edition)

A full-stack Netflix-style web application featuring user registration/login and movie browsing using TMDB API.
**Now powered by MongoDB Atlas!**

## Features
- **User Authentication**: Secure registration and login with password hashing.
- **Dynamic Content**: Fetches trending movies daily from TMDB API.
- **Responsive Design**: Dark-themed, mobile-friendly UI inspired by Netflix.
- **Database**: MongoDB Atlas (Cloud) integration for persistent user storage.

## Prerequisites
- Python 3.x
- [MongoDB Atlas Account](https://www.mongodb.com/cloud/atlas) (Free Tier is fine)
- TMDB API Key (Get one from [themoviedb.org](https://www.themoviedb.org/documentation/api))

## Installation & Setup

1.  **Clone/Open the Project**:
    Ensure you are in the project directory: `c:\Users\SHAIK FARHAN\Desktop\Netflix`

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configuration**:
    - Create a `.env` file by copying the example:
      ```bash
      copy .env.example .env
      ```
    - Open `.env` and fill in your details:
      - `MONGO_URI`: Your MongoDB Atlas connection string.
      - `TMDB_API_KEY`: Your API key from TMDB.
      - `SECRET_KEY`: Generate a random string.

    > **How to get your MONGO_URI:**
    > 1. Go to MongoDB Atlas -> Database -> Connect.
    > 2. Choose "Drivers" -> "Python" -> Version "3.12 or later".
    > 3. Copy the string. It looks like: `mongodb+srv://<user>:<password>@cluster0.abcde.mongodb.net/?retryWrites=true&w=majority`
    > 4. **Replace `<password>` with your actual database user password!**

4.  **Run the Application**:
    ```bash
    python app.py
    ```

5.  **Access the App**:
    - Open your browser and go to: `http://127.0.0.1:5000`

## Deployment (Render/Railway)

### Deployment on Render/Railway
1.  Push this code to a GitHub repository.
2.  Create a new Web Service.
3.  Add your Environment Variables: `MONGO_URI`, `TMDB_API_KEY`, `SECRET_KEY`.
4.  Render/Railway will automatically install dependencies from `requirements.txt`.
