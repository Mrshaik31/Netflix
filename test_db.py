from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

print("--- MongoDB Atlas Connection Test ---")

if not MONGO_URI:
    print("ERROR: MONGO_URI variable not found in .env file.")
else:
    # Mask password for display safety
    try:
        masked_uri = MONGO_URI.split('@')[1] if '@' in MONGO_URI else 'Invalid Format'
        print(f"Testing connection to: ...@{masked_uri}")
    except:
        print("Testing connection...")

    try:
        # Create a client
        client = MongoClient(MONGO_URI)
        
        # The 'ping' command is cheap and confirms a connection
        client.admin.command('ping')
        
        print("\nSUCCESS: Connected to MongoDB Atlas!")
        print(f"Server version: {client.server_info()['version']}")
        print("\nAvailable Databases:")
        for db_name in client.list_database_names():
            print(f" - {db_name}")

    except Exception as e:
        print(f"\nERROR: Connection failed!")
        print(f"Details: {e}")
        print("\nTroubleshooting tips:")
        print("1. Check your IP Whitelist in MongoDB Atlas (Network Access -> Add IP Address -> Allow Access from Anywhere).")
        print("2. Verify your username and password in the connection string.")
        print("3. Ensure you are not behind a corporate firewall blocking port 27017.")
