import os
import logging
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError, RPCError, PhoneCodeInvalidError, PhoneCodeExpiredError
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load API credentials from .env file
load_dotenv()

# Fetch API credentials securely
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

def check_credentials():
    """Check if API_ID and API_HASH are set."""
    if API_ID is None or API_HASH is None:
        logging.error("API_ID or API_HASH is not set in the .env file.")
        return False
    return True

def create_session(session_name):
    """Create a Telegram session file."""
    try:
        # Check for valid API credentials
        if not check_credentials():
            return

        # Check if session file already exists
        if os.path.exists(f"{session_name}.session"):
            logging.warning(f"Session file '{session_name}.session' already exists.")
            return

        # Create a Telegram client using API credentials from the .env file
        client = TelegramClient(session_name, int(API_ID), API_HASH)

        # Start the client, prompting the user for authentication
        with client:
            if client.is_user_authorized():
                logging.info(f"Session file '{session_name}.session' created successfully!")
                return
            
            # Request the user's phone number
            phone = input("Please enter your phone (or bot token): ")
            client.send_code_request(phone)
            code = input("Enter the code you received: ")

            try:
                client.sign_in(phone, code)
                logging.info(f"Session file '{session_name}.session' created successfully!")
            except SessionPasswordNeededError:
                password = input("Please enter your password: ")
                client.sign_in(phone, code, password=password)
                logging.info(f"Session file '{session_name}.session' created successfully!")
            except (PhoneCodeInvalidError, PhoneCodeExpiredError):
                logging.error("The code you entered is invalid or has expired. Please try again.")
            except RPCError as e:
                logging.error(f"RPC Error occurred: {e}")
            except Exception as e:
                logging.error(f"An error occurred during authentication: {e}")

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Get the desired session file name from the user
    session_name = input("Enter the desired session file name (without extension): ")

    # Create the session
    create_session(session_name)
