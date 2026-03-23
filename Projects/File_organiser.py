'''
minute fixing is to be done to this project
'''
import os
import shutil

folder_path = input("Enter your path file: ")

files =os.listdir(folder_path)

for file in files:
    images_path = folder_path + "/Images"
    docs_path = folder_path + "/Documents"
    code_path = folder_path + "/Source_Codes"
    other_path = folder_path + "/Others"

    source = folder_path + "/" + file
    
    if file.endswith(".jpg") or file.endswith(".png"):
      destination = images_path + "/" + file
      shutil.move(source, destination)


    elif file.endswith(".txt") or file.endswith(".pdf"):
      destination = docs_path + "/" + file
      shutil.move(source, destination)

    elif file.endswith(".py") or file.endswith(".cpp"):
        print(file, "-> Source Codes")

    else:
        print(file, "-> Other")            
if not os.path.exists(images_path):
    os.mkdir(images_path)

if not os.path.exists(docs_path):
    os.mkdir(docs_path)

if not os.path.exists(code_path):
    os.mkdir(code_path)

if not os.path.exists(other_path):
    os.mkdir(other_path)
             

