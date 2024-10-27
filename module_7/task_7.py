import csv
import hashlib
import re
import time

PATH_TO_FILE = '../module_6/feed.txt'
CSV_FILE = 'result.csv'
HEADERS = ['word', 'count']

def get_file_hash(_file_path):
    try:
        with open(_file_path, 'rb') as file:
            _file_hash = hashlib.md5(file.read()).hexdigest()
        return _file_hash
    except FileNotFoundError:
        print(f"File '{_file_path}' does not exist.")
        return None

def has_file_content_changed(_file_path, _last_hash):
    _current_hash = get_file_hash(_file_path)
    return _current_hash != _last_hash, _current_hash

def put_word(_filename, _word):
    _rows = []
    _word_found = False

    # Read existing CSV
    with open(_filename, 'r') as _file:
        _reader = csv.DictReader(_file)

        # If row found - add row with incremented count
        for _row in _reader:
            if _row['word'] == _word:
                _row['count'] = int(_row['count']) + 1
                _word_found = True
            _rows.append(_row)

        # If row NOT found - add row with count == 1
        if not _word_found:
            _rows.append({'word': _word, 'count': 1})

    # Write all the rows
    with open(_filename, 'w+') as _file:
        _writer = csv.DictWriter(_file, HEADERS)
        _writer.writeheader()
        _writer.writerows(_rows)

def start_csv_processing():
    # Clear CSV file before processing
    with open(CSV_FILE, 'w') as _file:
        _writer = csv.DictWriter(_file, HEADERS)
        _writer.writeheader()

    # Get all words in lowercase
    with open(PATH_TO_FILE, 'r') as feed_file:
        all_words = re.findall(r'\b[a-zA-z]+\b', feed_file.read().lower())

    # Process every word and pu into CSV file
    for w in all_words:
        put_word(CSV_FILE, w)

if __name__ == '__main__':
    last_hash = get_file_hash(PATH_TO_FILE)
    start_csv_processing()

    while True:
        time.sleep(1)
        file_changed, last_hash = has_file_content_changed(PATH_TO_FILE, last_hash)
        if file_changed:
            print("File content has been modified. Starting CSV processing")
            start_csv_processing()
