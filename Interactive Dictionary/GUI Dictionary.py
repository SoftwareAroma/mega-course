from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
import json
from difflib import get_close_matches

# creating the main window
root = tk.ThemedTk()
root.get_themes()  # Returns a list of all themes that can be set
root.set_theme("radiance")  # Sets an available theme radiance, clearlooks, plastik
root.title("Local Dictionary")
root.geometry("450x450")
root.resizable(False, False)

data = json.load(open("Data/data.json"))


def yes_btn():
    user_word = user_input.get()
    user_word = user_word.lower()
    definition = data[get_close_matches(user_word, data.keys())[0]]
    if type(definition) == list:
        for item in definition:
            meaning.insert(1.0, item + "\n")
            prompt["text"] = " "
            prompt1["text"] = " "
    else:
        meaning.insert(1.0, definition)
        prompt["text"] = " "
        prompt1["text"] = " "


def no_btn():
    error_message = "Word not found. Check the word again"
    prompt["text"] = error_message
    prompt1["text"] = " "
    meaning.delete(1.0, END)


# The functionality of the app
def find_meaning():
    user_word = user_input.get()
    user_word = user_word.lower()
    if user_word in data:
        definition = data[user_word]
        if type(definition) == list:
            for item in definition:
                meaning.insert(1.0, item + "\n")
                prompt["text"] = " "
                prompt1["text"] = " "
        else:
            meaning.insert(1.0, definition)
            prompt["text"] = " "
            prompt1["text"] = " "
    elif len(get_close_matches(user_word, data.keys())) > 0:
        alt = "Did you mean {alt_word}".format(alt_word=get_close_matches(user_word, data.keys())[0])
        prompt["text"] = alt
        prompt1["text"] = "click 'Yes' or 'No' to continue"
    else:
        error_message = "Word not found. Check the word again"
        prompt["text"] = error_message
        meaning.delete(1.0, END)


# the test field
inst = ttk.Label(root, text="Enter a word to find the meaning")
inst.place(x=110, y=10)

# input field for the word
user_input = ttk.Entry(root, width=40)
user_input.place(x=20, y=58)

# the go button
find_meaning = ttk.Button(root, text="Search", command=find_meaning)
find_meaning.place(x=300, y=50)

# the prompt for emergencies
prompt = ttk.Label(root, text=" ")
prompt.place(x=20, y=100)

# requesting for a no or yes to a suggestion
prompt1 = ttk.Label(root, text=" ")
prompt1.place(x=20, y=130)

yes_btn = ttk.Button(root, text="Yes", command=yes_btn)
yes_btn.place(x=300, y=90)

no_btn = ttk.Button(root, text="No", command=no_btn)
no_btn.place(x=300, y=130)

# the area for displaying the message
meaning = Text(root, width=53, height=15)
meaning.place(x=10, y=170)

# the status bar
status_bar = Label(root, text="Welcome to mia dictionary", relief=SUNKEN)
status_bar.pack(side=BOTTOM, fill=X)

root.mainloop()
