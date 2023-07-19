import json
import os
import sqlite3


def process_one_file(file):
    with open(os.path.join(dir_path, file), 'r', encoding='utf-8') as f:
        data = json.load(f)
        json_list.append(data)



def insertFromDict(table, dict):
    sql = 'INSERT INTO ' + table
    sql += ' (' + ', '.join(escapeDictKey(dict)) + ')'
    sql += ' VALUES (' + ', '.join(map(dictValuePad, dict.values())) + ');'
    return sql


def escapeDictKey(dict):
    new_dict = {}
    for key, value in dict.items():
        key = '"' + key + '"'
        new_dict[key] = value
    return new_dict


def dictValuePad(value):
    if isinstance(value, bool):
        return "'" + str(value) + "'"
    elif isinstance(value, int):
        return str(value)
    elif isinstance(value, dict):
        return "\"" + str(value) + "\""
    elif isinstance(value, list):
        return "\"" + str(value) + "\""
    else:
        return "'" + str(value) + "'"


# connect database

conn = sqlite3.connect("taiwu.db")
cursor = conn.cursor()



#  list all directories in a path
path = 'C:/Users/Administrator/Desktop/sql/taiwuDataDump'
directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
print(directories)

# loop through all directories and load json files in each  dictionaries
for tab in directories:
    dir_path = os.path.join(path, tab)
    json_files = [pos_json for pos_json in os.listdir(dir_path) if pos_json.endswith('.json')]
    json_list = []
    for file in json_files:
        process_one_file(file)
    # step 3 go through all the files, generate a INSERT INTO SQL
    for i in range(len(json_list)):
        sql = insertFromDict(f'{tab}', json_list[i])
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




