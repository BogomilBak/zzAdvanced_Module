import re
from string import punctuation
with open('./text.txt', 'r') as words_file:
    text = words_file.readlines()


with open('./output.txt', 'w') as output_file:
    for line in range(len(text)):
        current_line = text[line]
        count_letters = 0
        count_punctuation = 0
        for word in text[line]:
            if word.isalpha():
                count_letters += 1
            elif word in punctuation:
                count_punctuation += 1
        output_file.write(f"Line {line + 1}: {''.join(text[line][:-1])} ({count_letters})({count_punctuation})\n")