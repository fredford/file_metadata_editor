

import sys
import os

import tkinter as tk

from utilities import exit_app, get_directory_contents, select_folder, update_file_information, update_folder_information



class App:

    def run(self):

        folder_path = ""

        while True:
            # Allow the User to select a folder to perform operations on
            folder_path = select_folder(folder_path)

            # Check that the directory supplied is valid
            if os.path.isdir(folder_path):
                files, folders = get_directory_contents(folder_path)
            else:
                print("Invalid directory path. Closing.")
                break

            # Update the information for the folders in the directory
            update_folder_information(folders)

            # Update the information for the files in the directory
            update_file_information(files)

            # Exit application
            if exit_app():
                break



# def exit_app():
#     root.quit()

# root = tk.Tk()
# root.withdraw()

# folder_path = select_folder()

# print(type(folder_path))

# if os.path.isdir(folder_path):
#     contents = os.listdir(folder_path)

#     files = []
#     folders = []

#     for item in contents:
#         item_path = os.path.join(folder_path, item)
#         if os.path.isfile(item_path):
#             files.append(item)
#         elif os.path.isdir(item_path):
#             folders.append(item)

#     print("-----Files-----")
#     for file in files:
#         print(file)

#     print("-----Folders-----")
#     for folder in folders:
#         print(folder)

# else:
#     print("Invalid directory path. Please try again")


# exit_button = tk.Button(root, text="Exit", command=exit_app)
# exit_button.pack()

# root.mainloop()

# TODO Things that need to get done

if __name__ == "__main__":
    app = App()
    app.run()
