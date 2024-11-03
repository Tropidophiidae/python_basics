import json
import os

from module_6.task_6 import get_records_to_export, get_file_path



if __name__ == '__main__':
    while True:
        print('-------------------')
        count = get_records_to_export()
        if count == 0:
            continue

        file_path = get_file_path('feed.json')
        if file_path is None:
            continue

        print(f"Opening the file: {file_path}")
        json_file = json.load(open(file_path))
        if count > len(json_file):
            print(f"Selected file contains only {len(json_file)} records. Please try again")
            continue
        for i in range(0, count):
            record = json_file[i]
            print(f">>>>>>Record #{i+1}<<<<<<")
            print(f"{record['type']}\n{record['text']}\n{record['unique_part']}")

        print('-------------------')
        print('Reading finished')
        print(f"Removing file {file_path}")
        os.remove(file_path)