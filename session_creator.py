import os
from telethon import TelegramClient
from dotenv import load_dotenv

# Load API credentials from .env file
load_dotenv()

# Fetch API credentials securely
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

# Function to create a Telegram session file
def create_session(session_name):
    # Check if session file already exists
    if os.path.exists(f"{session_name}.session"):
        print(f"Session file '{session_name}.session' already exists.")
        return

    # Create a Telegram client using API credentials from the .env file
    client = TelegramClient(session_name, API_ID, API_HASH)

    # Start the client, prompting the user for authentication
    with client:
        print(f"Session file '{session_name}.session' created successfully!")

if __name__ == "__main__":
    # Get the desired session file name from the user
    session_name = input("Enter the desired session file name (without extension): ")

    # Create the session
    create_session(session_name)
