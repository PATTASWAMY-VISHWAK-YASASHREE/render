import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

# Import the Flask app
from app import app as application

# Make app available for gunicorn
app = application
