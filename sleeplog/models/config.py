import os
# In [dev] setup try to import from .env
try:
    import dotenv
    dotenv.load_dotenv()
except ImportError:
    pass

# Authentication
authtkt_secret = os.environ['AUTHTKT_SECRET']

# Session
session_secret = os.environ['SESSION_SECRET']

# Google OAuth 2.0 for Login
google_client_id = os.environ['GOOGLE_CLIENT_ID']
google_client_secret = os.environ['GOOGLE_CLIENT_SECRET']
google_project_id = os.environ['GOOGLE_PROJECT_ID']
google_token_uri = os.environ['GOOGLE_TOKEN_URI']
