Easily generate Telegram session files with custom names using Python's Telethon library. This project securely stores your 'Telegram API' credentials in a '.env' file, protecting your sensitive information. Simple setup with detailed instructions for 'Linux', 'Windows', and 'macOS'. Ideal for developers automating 'Telegram bots' or managing multiple accounts.

# Telegram Session Creator

This project allows you to create a Telegram session file using the `Telethon` library. The session file stores your Telegram login credentials securely and can be customized with a user-defined file name. API credentials are stored securely in a `.env` file.

## Features
- Customizable session file names
- Secure API credential storage using `.env`
- Compatible with Linux, Windows, and macOS

## Requirements
- Python 3.x
- Telegram API credentials (API ID and API Hash)

## Getting Your Telegram API Credentials
To use this script, you'll need your API ID and API Hash from [my.telegram.org](https://my.telegram.org).
1. Log in to [my.telegram.org](https://my.telegram.org).
2. Go to **API Development Tools**.
3. Create a new application and note your **API ID** and **API Hash**.

## Setup Instructions

### 1. Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/py-hariom/telegram-session-maker.git
```
then
```
cd telegram-session-maker
```

### 2. Set Up a Virtual Environment
A virtual environment helps isolate dependencies for this project. Follow the steps below for your OS:

#### Linux & macOS:
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

#### Windows:
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate
```

### 3. Install the Requirements
Once the virtual environment is activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Create the `.env` File
You need to create a `.env` file to securely store your Telegram API credentials.

#### Linux & macOS:
You can use `nano` or any other text editor to create the file:
```bash
nano .env
```

#### Windows:
You can create the file using Notepad:
```bash
notepad .env
```

In the `.env` file, add your API ID and API Hash like this:
```env
API_ID = Paste_her_your_api_id
API_HASH = Paste_her_your_api_hash
```

Replace `Paste_her_your_api_id` and `Paste_her_your_api_hash` with your actual credentials.

### 5. Running the Script
To create a Telegram session file with a custom name:

#### Linux & macOS:
```bash
python3 session_creator.py
```

#### Windows:
```bash
python session_creator.py
```

You will be prompted to enter the desired session file name. The session file will be created with the `.session` extension in your current directory.

### 6. Deactivating the Virtual Environment
When you're done, you can deactivate the virtual environment:

#### Linux & macOS:
```bash
deactivate
```

#### Windows:
```bash
venv\Scripts\deactivate
```

## File Structure

```bash
telegram-session/
│
├── .env               # Stores API credentials (ignored by Git)
├── .gitignore         # Ensures sensitive files like .env are not pushed to GitHub
├── requirements.txt   # Lists the dependencies
├── session_creator.py # The main Python script for creating session files
└── README.md          # Project documentation
```

## Additional Information

### Updating Dependencies
If you add any additional libraries or need to update the dependencies in `requirements.txt`, run:
```bash
pip freeze > requirements.txt
```

### Security
- **DO NOT** share your `.env` file or session files publicly.
- Ensure your `.env` file is included in `.gitignore` so it’s not accidentally pushed to GitHub.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

### Key Steps Covered:
1. Cloning the repository.
2. Creating a virtual environment for isolating dependencies.
3. Installing required dependencies from `requirements.txt`.
4. Using `.env` to store sensitive data (API ID and API Hash).
5. Running the script and deactivating the virtual environment when finished.
6. File structure and security tips.
