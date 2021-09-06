import os

# application settings
MONGO_URL = 'mongodb://127.0.0.1:27017/index'

# Generate a random secret key
SECRET_KEY = os.urandom(24)
CSRF_ENABLED = True
