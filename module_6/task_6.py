import os
import module_3.task_3 as case_normalization


def normalize_case(_line):
    return case_normalization.capitalize_first_char_in_the_line(case_normalization.capitalize_after_dot(_line))

def get_records_to_export():
    input_records_count = input('Number of records to export: ')
    if not input_records_count.isdigit() or input_records_count == 0:
        print(f">>>Entered value ('{input_records_count}') is not valid integer<<<")
        return 0
    return int(input_records_count)

def get_file_path(default_file):
    input_file_path = input('Provide path to the file or left empty for the current folder: ')
    if input_file_path == '':
        input_file_path = os.getcwd() + '\\' + default_file
        print(f"Current folder is selected")
        if not os.path.exists(input_file_path) and not os.path.isfile(input_file_path):
            print(f"The file '{input_file_path}' does not exist or is not a file.")
            return None
    return input_file_path


if __name__ == '__main__':
    while True:
        print('-------------------')
        count = get_records_to_export()
        if count == 0:
            continue

        file_path = get_file_path('feed.txt')
        if file_path is None:
            continue

        print(f"Opening the file: {file_path}")
        with open(file_path, 'r+') as file:
            content = file.read()  # Reads the entire file content

        content_lines = content.splitlines()
        start_line = 0
        lines_processed = 0
        for i, line in enumerate(content_lines):
            if lines_processed >= count:
                print(f"The limit is reached: {count}")
                break
            # If end of the record found
            if line == '':
                # Collect all the lines to 'result' variable
                while start_line < i:
                    print(normalize_case(content_lines[start_line].lower()))
                    start_line += 1
                # To skip empty line between records
                start_line += 1
                lines_processed += 1
                print('-------------------------------')

        print("Removing file")
        os.remove(file_path)