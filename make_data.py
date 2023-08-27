import os
import json 

# directory/folder path
dir_path = 'flowers/'

# list to store files
res = []

# Iterate directory
for file_path in os.listdir(dir_path):
    # check if current file_path is a file
    if os.path.isfile(os.path.join(dir_path, file_path)) and ".DS_Store" not in file_path:
        # add filename to list
        res.append(file_path)
      
# Serializing json  
json_object = json.dumps(res, indent = 4) 
print(json_object)