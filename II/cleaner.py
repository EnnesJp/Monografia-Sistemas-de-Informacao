import os

DIR = "./database"
FIND_PREFIX = 'ATOM'
FILE_EXT = '.pdb'

def clean_files():
  try:
    for filename in os.listdir(DIR):
      if filename.endswith(FILE_EXT):
        with open(filename, 'r') as fr:
          lines = fr.readlines()

          with open(filename, 'w') as fw:
            for line in lines:

              if line.startswith(FIND_PREFIX):
                  fw.write(line)
          print(filename + " clean!")
  except:
    print("Oops! someting error")
    
clean_files()