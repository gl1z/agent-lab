from datetime import datetime
from langchain_core.tools import tool

@tool
def get_current_time() -> str:
    """Returns the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
@tool
def read_notes_file() -> str:
    """Reads and returns the contents of the notes.txt file."""
    try:
        with open("notes.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "notes.txt not found."