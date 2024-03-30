import os
from dotenv import load_dotenv

def get_env_variables():
    """Get the environment variables."""
    load_dotenv()
    return dict({
        'DB_NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
        'OPTIONS': os.getenv('OPTIONS')
    })
