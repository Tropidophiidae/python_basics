import os
import xml.etree.ElementTree as ET

from module_6.task_6 import get_records_to_export, get_file_path

if __name__ == '__main__':
    while True:
        print('-------------------')
        count = get_records_to_export()
        if count == 0:
            continue

        file_path = get_file_path('feed.xml')
        if file_path is None:
            continue

        print(f"Opening the file: {file_path}")
        xml_file = ET.parse(file_path).getroot()
        if count > len(xml_file):
            print(f"Selected file contains only {len(xml_file)} records. Please try again")
            continue

        for i in range(0, count):
            print(f">>>>>>Record #{i + 1}<<<<<<")
            for child in xml_file[i]:
                print(f"{child.text}")

        print('-------------------')
        print('Reading finished')
        print(f"Removing file {file_path}")
        os.remove(file_path)