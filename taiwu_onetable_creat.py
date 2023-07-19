import json
import os
import pandas as pd
import sqlite3

# connect database

conn = sqlite3.connect("C:\\Users\\Administrator\\Desktop\\python 100\\taiwu.db")
cursor = conn.cursor()
cursor.execute('''DROP TABLE IF EXISTS ArmorItem''')


# directory containing JSON files
dir_path = 'C:/Users/Administrator/Desktop/sql/taiwuDataDump/ArmorItem'

# list of JSON files in directory
json_files = [pos_json for pos_json in os.listdir(dir_path) if pos_json.endswith('.json')]
# print(json_files)

# loop through JSON files and load them into Python dictionaries
json_list = []


def process_one_file(file):
    with open(os.path.join(dir_path, file), 'r', encoding='utf-8') as f:
        data = json.load(f)
        json_list.append(data)


for file in json_files:
    process_one_file(file)


#  step1 go through all the files and find out all unique keywords

keywords=[]
new_dictionary = {}
for i in range(len(json_list)):
    for key, value in json_list[i].items():
        if key not in keywords:
            keywords.append(key)
            new_dictionary[key] = value
# print(keywords)
# print(new_dictionary)




## step 2 base on new_dictionary, generate a CREATE TABLE SQL

key_type = []
for key, value in new_dictionary.items():
    if isinstance(value, bool):
        key_type.append(key+' TEXT')
    elif isinstance(value, int):
        key_type.append(key + ' NUMERIC')
    else:
        key_type.append(key+' TEXT')
table_column = ",".join(key_type)
print(f"create table ArmorItem({table_column}) ")
cursor.execute(f"create table ArmorItem({table_column}); ")


cursor.close()
conn.commit()
conn.close()
# convert list of JSON dictionaries to Pandas DataFrame
#df = pd.DataFrame.from_records(json_list)
#df.to_csv('C:/Users/Administrator/Desktop/sql/taiwuDataDump/AccessoryItem/output.csv', index=False)
# print DataFrame




