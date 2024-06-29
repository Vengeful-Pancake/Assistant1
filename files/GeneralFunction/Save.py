import json

def SAVE(value, replace, path):
    #save from program to data file
    path="lesser_data\\Resources\\Save\\"+path+".txt"
    with open(path, "r") as f:
        savedfile = f.read()
    loadedfile = json.loads(savedfile)
    loadedfile.update({replace:value})
    loadedfile = json.dumps(loadedfile)
    
    #format
    loadedfile = loadedfile.replace(''', "''',''',\n  "''')
    loadedfile = loadedfile.replace('''{"''','''{\n  "''')
    loadedfile = loadedfile.replace('''}''','''\n}''')
    
    with open(path, "w") as f:
        f.write(loadedfile)
    print ("Successfully saved " + str(value) + " into " + replace + ".")

def LOAD(value, path):
    #load from data file to program
    path="lesser_data\\Resources\\Save\\"+path+".txt"
    with open(path, "r") as f:
        savedfile = f.read()
    loadedfile = json.loads(savedfile)
    print ("Successfully loaded " + value + ".")
    return(loadedfile[value])

def DEFAULT(path):
    path_default="lesser_data\\Resources\\Save\\"+path+"default.txt"
    path="lesser_data\\Resources\\Save\\"+path+".txt"
    with open(path_default, "r") as f:
        saved_file_default = f.read()
    loaded_file_default = json.loads(saved_file_default)
    loaded_file_default = json.dumps(loaded_file_default)
    loaded_file_default = loaded_file_default.replace(''', "''',''',\n  "''')
    loaded_file_default = loaded_file_default.replace('''{"''','''{\n  "''')
    loaded_file_default = loaded_file_default.replace('''}''','''\n}''')
    with open(path, "w") as f:
        f.write(loaded_file_default)
    print ("Successfully return to default.")
    