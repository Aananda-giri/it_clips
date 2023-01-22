import pyperclip
import datetime
import json
import os
import sys
sys.path.append("/home/sec/.local/lib/python3.9/site-packages")


current_file_path = os.path.abspath(__file__).replace('clips.py', '')
# print(current_file_path)

try:
    # Get File path from user
    FILE_NAME = current_file_path + sys.argv[1] + '.json'
except IndexError:
    # default file name if no file name is provided
    FILE_NAME = current_file_path + 'clips.json'

# print(FILE_NAME)
if os.path.exists(FILE_NAME):
    # load previous DATA
    with open(FILE_NAME, 'r') as f:
        DATA = json.load(f)
else:
    DATA = []

def write_to_file(text=''):
    if text != '':
        # Add current clip to previus list
        DATA.append(text)

    # write to file
    with open(FILE_NAME, 'w') as f:
        json.dump(DATA, f)

def main():
    previous_clipboard = {}
    while True:
        current_clipboard = pyperclip.paste()
        if current_clipboard != previous_clipboard:
            write_to_file(current_clipboard)
            previous_clipboard = current_clipboard

if __name__=="__main__":
    try:	
        main()
    except KeyboardInterrupt:
        # user press ctrl + c: saving andexisting code
        write_to_file()
        print("Keyboard interrupt detected, exiting program.")
        sys.exit()
