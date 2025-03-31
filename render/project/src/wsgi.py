import os
import sys

# Get the absolute path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the current directory to Python path
sys.path.insert(0, current_dir)

# Now try to import the app
from app import app as application

# For compatibility with different WSGI servers
<<<<<<< Updated upstream
<<<<<<< Updated upstream
app = application
=======
app = application
>>>>>>> Stashed changes
=======
app = application
>>>>>>> Stashed changes
