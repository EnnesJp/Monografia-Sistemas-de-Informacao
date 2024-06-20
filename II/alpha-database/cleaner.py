import os

DIR = "./"
FIND_PREFIX = 'ATOM'

def clean_files():
  try:
    for name in os.listdir(DIR):
      if name != '.DS_Store' and name != 'cleaner.py':
        for filename in os.listdir(os.path.join(DIR, name)):
          with open(os.path.join(DIR, name, filename), 'r') as fr:
            lines = fr.readlines()

            with open(os.path.join(DIR, name, filename), 'w') as fw:
              for line in lines:

                if line.startswith(FIND_PREFIX):
                    fw.write(line)

        print(filename + " clean!")
  except:
    print("Oops! someting error")
    
clean_files()