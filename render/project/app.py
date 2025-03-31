# This is just a proxy to import the real app
import sys
import os

# Add the src directory to Python's path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

# Import the real app
from app import app
