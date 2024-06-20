import os

DIR = "./alpha-database"
REMOVE_EXT = ".cif"

def remove_files():
  try:
    for name in os.listdir(DIR):
        if name != '.DS_Store' and name != 'cleaner.py':
          for filename in os.listdir(os.path.join(DIR, name)):
              if not filename.endswith(REMOVE_EXT):
                os.remove(os.path.join(DIR, name, filename))
                
        print(name + " clean!")
  except:
    print("Oops! someting error")
    
remove_files()