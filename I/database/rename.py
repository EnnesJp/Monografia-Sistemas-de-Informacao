import os

REMOVE_WORD = "pdb"
REMOVE_EXT = ".ent"

def change_extension():
    for filename in os.listdir("."):
      if filename.suffix == REMOVE_EXT:
          os.rename(filename, filename.with_suffix('.pdb').name)
  
def remove_start():
  for filename in os.listdir("."):
    if filename.startswith(REMOVE_WORD):
      os.rename(filename, filename[len(REMOVE_WORD):])
    