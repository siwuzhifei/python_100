import json
import os
import sqlite3

def process_one_file(file):
    with open(os.path.join(dir_path, file), 'r', encoding='utf-8') as f:
        data = json.load(f)
        json_list.append(data)

# connect database

conn = sqlite3.connect("taiwu.db")
cursor = conn.cursor()
# cursor.execute('''DROP TABLE IF EXISTS ArmorItem''')

#  list all directories in a path
path = 'C:/Users/Administrator/Desktop/sql/taiwuDataDump'

directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
print(directories)

for tab in directories:
    dir_path = os.path.join(path, tab)
    json_files = [pos_json for pos_json in os.listdir(dir_path) if pos_json.endswith('.json')]
    json_list = []
    keywords = []
    new_dictionary = {}
    for file in json_files:
        process_one_file(file)
    #  step1 go through all the files and find out all keywords
    for i in range(len(json_list)):
        for key, value in json_list[i].items():
            key = '"'+ key+'"'
            keywords.append(key)
            new_dictionary[key] = value
    ## step 2 base on new_dictionary, generate a CREATE TABLE SQL
    key_type = []
    for key, value in new_dictionary.items():
        if isinstance(value, bool):
            key_type.append(key + ' TEXT')
        elif isinstance(value, int):
            key_type.append(key + ' NUMERIC')
        else:
            key_type.append(key + ' TEXT')
    table_column = ",".join(key_type)
    print(f"create table {tab}({table_column}) ")
    cursor.execute(f'''DROP TABLE IF EXISTS {tab}''')
    try:
        cursor.execute(f"create table {tab}({table_column}); ")
    except:
        print('something goes wrong!')
        pass





cursor.close()
conn.commit()
conn.close()
# convert list of JSON dictionaries to Pandas DataFrame
#df = pd.DataFrame.from_records(json_list)
#df.to_csv('C:/Users/Administrator/Desktop/sql/taiwuDataDump/AccessoryItem/output.csv', index=False)
# print DataFrame




