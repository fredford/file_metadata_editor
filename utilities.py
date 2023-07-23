# Utilities.py
#
# This file contains helper functions that are used in the file editing process.

from tkinter import filedialog

def select_folder(initial_dir=""):
    """
    This opens a file dialog window allowing the user to select a folder. The function returns the folder path as a string.

    Returns:
        string: The path of the selected folder.
    """
    folder_path = filedialog.askdirectory(initialdir=initial_dir)
    print("Folder Path: ", folder_path)
    return folder_path

def get_directory_contents(path):
    return [], []

def update_folder_information():
    pass

def update_file_information():
    pass


def exit_app():
    """
    Prompt the user to confirm application exit.

    This function displays a prompt to the user, asking if they want to quit the application.
    The user is expected to input either 'y' (yes) or 'n' (no) to confirm or cancel the exit.

    Returns:
        bool: True if the user confirms to quit (inputs 'y'), False otherwise (inputs 'n').

    Example:
        >>> if exit_app():
        ...     print("Exiting the application...")
        ... else:
        ...     print("Continuing with the application.")
    """
    return input("Quit (y or n): ") == "y"


class Folders:
    def __init__(self, items=[]):
        self.items = items

class Files:
    def __init__(self, items=[]):
        self.items = items
