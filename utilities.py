# utilities.py
#
# This file contains helper functions that are used in the file editing process.

import os

from classes.folders import Folders
from classes.documents import Documents
from classes.document import Document
from classes.folder import Folder

from tkinter import filedialog

def select_folder(initial_dir=""):
    """
    This function opens a file dialog window allowing the user to select a folder. The function returns the folder path as a string.

    Returns:
        string: The path of the selected folder.
    """
    folder_path = filedialog.askdirectory(initialdir=initial_dir)
    print("Folder Path: ", folder_path)
    return folder_path

def get_directory_contents(path):

    """
    This function retrieves the contents of the provided path, sorts them into folders and files and instantiates them as Folder or File objects.

    Returns:
        Items: The object containing the files in the given directory
        Folders: The object containing the folders in the given directory
    """

    documents = Documents()
    folders = Folders()

    contents = os.listdir(path)

    for item in contents:
        item_path = os.path.join(path, item)
        # Check if the item is a file
        if os.path.isfile(item_path):
            document = Document(item, item_path)
            documents.add_item(document)
            document.print()
        # Check if the item is a folder
        elif os.path.isdir(item_path):
            folder = Folder(item, item_path)
            folders.add_item(folder)
            folder.print()

    return documents, folders

def update_folder_information(folders):
    pass

def update_file_information(files):
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


