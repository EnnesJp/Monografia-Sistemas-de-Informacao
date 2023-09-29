import os

DIR = "."

REMOVE_WORD = "pdb"
REMOVE_EXT = ".ent"

NEW_EXT = ".pdb"

def change_extension():
  for filename in os.listdir(DIR):
    if filename.endswith(REMOVE_EXT):
      new_file = filename[:len(REMOVE_EXT)]
      os.rename(filename, new_file + NEW_EXT)
  
def remove_start():
  for filename in os.listdir(DIR):
    if filename.startswith(REMOVE_WORD):
      os.rename(filename, filename[len(REMOVE_WORD):])

remove_start()
change_extension()