import os

DIR = "./database"
FIND_PREFIX = 'ATOM'

def clean_files():
  try:
    for filename in os.listdir(DIR):
      with open(f'{DIR}/{filename}', 'r') as fr:
        lines = fr.readlines()

        with open(f'{DIR}/{filename}', 'w') as fw:
          for line in lines:

            if line.startswith(FIND_PREFIX):
                fw.write(line)
        print(filename + " clean!")
  except:
    print("Oops! someting error")
    
clean_files()