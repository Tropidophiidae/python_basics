import csv
import re
import time

import task_7_1 as task_7

CSV_FILE = 'result_2.csv'
HEADERS = ['letter', 'count_all', 'count_uppercase', 'percentage']


def put_letter(_filename, _letter):
    _rows = []
    _letter_count_dict = {}
    _letter_found = False
    _letter_upper = not _letter.islower()

    # Read existing CSV
    with (open(_filename, 'r') as _file):
        _reader = csv.DictReader(_file)

        # If row found - add row with incremented count
        for _row in _reader:
            if _row['letter'] == _letter or _row['letter'] == _letter.lower():
                _row['letter'] = _letter.lower()
                _row['count_all'] = int(_row['count_all']) + 1
                if _letter_upper:
                    _row['count_uppercase'] = int(_row['count_uppercase']) + 1
                _letter_found = True
            _rows.append(_row)

        # If row NOT found - add row with count == 1
        if not _letter_found:
            _count_uppercase = 1 if _letter_upper else 0
            _rows.append(
                {'letter': _letter.lower(), 'count_all': 1, 'count_uppercase': _count_uppercase, 'percentage': 0})

        # Get total value
        for _row in _rows:
            _letter_count_dict[_row['letter']] = int(_row['count_all'])
        _total = sum(_letter_count_dict.values())

        # Calculate percentages
        for _row in _rows:
            _row['percentage'] = (_letter_count_dict[_row['letter']] / _total) * 100

    # Write all the rows
    task_7.write_rows(_filename, _rows, HEADERS)


def start_csv_processing():
    task_7.initialize_csv(CSV_FILE)

    with open(task_7.PATH_TO_FILE, 'r') as feed_file:
        all_letters = re.findall(r'[a-zA-z]', feed_file.read())

    for l in all_letters:
        put_letter(CSV_FILE, l)


if __name__ == '__main__':
    last_hash = task_7.get_file_hash(task_7.PATH_TO_FILE)
    start_csv_processing()

    while True:
        time.sleep(1)
        file_changed, last_hash = task_7.has_file_content_changed(task_7.PATH_TO_FILE, last_hash)
        if file_changed:
            print("File content has been modified. Starting CSV processing")
            start_csv_processing()
