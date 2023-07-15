import os
import json



#  list all directories in a path
path = 'C:/Users/Administrator/Desktop/sql/taiwuDataDump'

directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
print(directories)


# loop through all directories and load json files in each  dictionaries
for i in directories:
    dir_path = os.path.join(path, i)
    json_files = [pos_json for pos_json in os.listdir(dir_path) if pos_json.endswith('.json')]
    json_list = []
    for file in json_files:
        with open(os.path.join(dir_path, file), 'r', encoding='utf-8') as f:
            data = json.load(f)
            json_list.append(data)




    # # convert list of JSON dictionaries to Pandas DataFrame
    # df = pd.DataFrame.from_records(json_list)
    # df.to_csv(os.path.join(dir_path, f"{i}.csv"), index=False)

