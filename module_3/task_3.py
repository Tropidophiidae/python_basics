import re

homework = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# TASK normalize - Issue Capitalize should be added after each dot
# apply lower() to all text
homework = homework.lower()


# TASK add new sentence in the end of 2nd paragraph
def capitalize_first_char_in_the_line(_line):
    # find first char in the line
    _match = re.search(r'\S', _line)
    # if found
    if _match is not None:
        # get char value
        first_char = _match.group()
        # replace first char with upper version
        return _line.replace(first_char, first_char.upper(), 1)


def get_last_word(_line):
    # find last word of each line. The logic is to find word between ' ' and last '.'
    last_dot = _line.rfind('.')
    # if last_dot is found
    if last_dot != -1:
        # split line into words, get last one and remove dot '.'
        return _line.split()[-1].replace('.', '')


def capitalize_after_dot(_line):
    result = []
    capitalize = False

    for char in _line:
        if capitalize and not char.isspace():
            result.append(char.upper())
            capitalize = False
        elif char == '.':
            capitalize = True
            result.append(char)
        else:
            result.append(char)

    return ''.join(result)


last_words = []
# cycle to get throw all the lines
homework_lines = homework.splitlines()
# cycle to go throw all the lines
for i, line in enumerate(homework_lines):
    # capitalize all the character after dot
    updated_line = capitalize_after_dot(line)

    # capitalize first character in the line
    updated_line = capitalize_first_char_in_the_line(updated_line)
    homework_lines[i] = updated_line if updated_line is not None else homework_lines[i]

    # get last word of each sentence
    last_word = get_last_word(line)
    if last_word is not None: last_words.append(last_word)

# capitalize first word of last_words list
last_words[0] = last_words[0].capitalize()
# add found last words to the end of 2nd paragraph
for word in last_words:
    homework_lines[3] += ' ' + word
# replace homework string with updated list of lines
homework = '\n'.join(homework_lines)

# TASK iZ
homework = homework.replace(' iz ', ' is ')

# TASK calculate number of whitespace characters
whitespace_count = len(re.findall(r'\s', homework))

print('=== number of all whitespaces ===')
print(whitespace_count)
print('=== formatted text ===')
print(homework)
