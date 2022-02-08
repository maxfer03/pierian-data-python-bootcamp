from dis import Instruction
import re
import shutil
from turtle import st
import zipfile, os

# we extract the data
zip = zipfile.ZipFile('unzip_me_for_instructions.zip', 'r')
zip.extractall("unzipped")

# we read the instructions
content_dir = "./unzipped/extracted_content"

inst = open(f'{content_dir}/Instructions.txt')
inst_data =  ''.join(inst.readlines())
print(inst_data)

# we walk the directories
regex = r'\d\d\d-\d\d\d-\d\d\d\d'
phone = ''
for folder, sub_folders, files in os.walk(content_dir):
    for file in files:
        textfile = open(folder+'/'+file)
        text = textfile.readline()
        # we search with a regex combination:
        try:
            search = re.search(regex, text)
            result = search.group()
            print(f'Match found at {file}! ---',result)
            phone = result
        except: 
            print(f'No matches at {file}')


print(f'\nPhone found: {phone}\n')

# we clean the folder
shutil.rmtree("./unzipped")