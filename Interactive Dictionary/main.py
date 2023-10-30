import json
from difflib import get_close_matches

data = json.load(open("data.json"))
word = input("Enter a word: ")
word = word.lower()


def define_word(W):
    if W in data:
        meaning = data[W]
        return meaning
    elif len(get_close_matches(W, data.keys())) > 0:
        alt = "Did you mean {alt_word}".format(alt_word=get_close_matches(W, data.keys())[0])
        print(alt)
        choice = str(input("Entr 'y' for 'Yes' or 'n' for 'No' : "))
        choice = choice.lower()
        if choice == 'y':
            return data[get_close_matches(W, data.keys())[0]]
        elif choice == 'n':
            return "Word not Found. Check the word again"
        else:
            return "Invalid input"
    else:
        error_message = "Word not Found. Check the word again"
        return error_message

definition = define_word(word)
if type(definition) == list:
    for item in definition:
        print(item)
else:
    print(definition)
