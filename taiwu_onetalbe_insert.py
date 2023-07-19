import json
import os
import sqlite3

# connect database

conn = sqlite3.connect("taiwu.db")
cursor = conn.cursor()



# directory containing JSON files
dir_path = 'C:/Users/Administrator/Desktop/sql/taiwuDataDump/ArmorItem'

# list of JSON files in directory
json_files = [pos_json for pos_json in os.listdir(dir_path) if pos_json.endswith('.json')]
print(json_files)

# loop through JSON files and load them into Python dictionaries
json_list = []


def process_one_file(file):
    with open(os.path.join(dir_path, file), 'r', encoding='utf-8') as f:
        data = json.load(f)
        json_list.append(data)


for file in json_files:
    process_one_file(file)


#  step1 go through all the files and find out all keywords

keywords=[]
new_dictionary = {}
for i in range(len(json_list)):
    for key, value in json_list[i].items():
        if key not in keywords:
            keywords.append(key)
            new_dictionary[key] = value
# print(keywords)
# print(new_dictionary)






def insertFromDict(table, dict):
    sql = 'INSERT INTO ' + table
    sql += ' (' + ', '.join(dict) + ')'
    sql += ' VALUES (' + ', '.join(map(dictValuePad, dict.values())) + ');'
    return sql

def dictValuePad(value):
    if isinstance(value, bool):
        return "'" + str(value) + "'"
    elif isinstance(value, int):
        return str(value)
    elif isinstance(value, dict):
        return '0'
    elif isinstance(value, list):
        return '0'
    else:
        return "'" + str(value) + "'"


# step 3 go through all the files, generate a INSERT INTO SQL
for i in range(len(json_list)):
    sql = insertFromDict('ArmorItem', json_list[i])
    print(sql)
    try:
        cursor.execute(sql)
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




