import os
import subprocess
import tkinter
from tkinter import filedialog

def set_openai_key():
    openai_key = os.environ.get("OPENAI_API_KEY")
    if openai_key is None or openai_key == "" or openai_key == "0":
        openai_key = input("Please enter your OPENAI_API_KEY: ")
        os.environ["OPENAI_API_KEY"] = openai_key
        # print(os.environ["OPENAI_API_KEY"])
    else:
        os.environ["OPENAI_API_KEY"] = openai_key
        # print(os.environ["OPENAI_API_KEY"])


def set_google_calendar_credentials():
    tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

    folder_path = filedialog.askopenfilename()
    if folder_path:  # Check if the user selected a file
        folder_path = folder_path.replace("/", "\\")  # Replace forward slashes with double backslashes

        # Remove the first and last characters
        # folder_path = repr(folder_path)
        folder_path = folder_path.replace("'", '"')
        # folder_path = folder_path[1:-1]

    return folder_path