"""
File handling utilities.
"""

import json
import os

FILE_NAME = "data/students.json"


def load_data():
    """Load student data from JSON file."""

    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_data(data):
    """Save student data to JSON file."""

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)