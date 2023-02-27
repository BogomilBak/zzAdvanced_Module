import re

result = {}
pattern = f'[a-zA-Z\']+'
with open('./words.txt', 'r') as words_file:
    all_words = words_file.read().split()
    for word in all_words:
        result[word.lower()] = 0

with open('./input.txt', 'r') as words_file:
    for line in words_file:
        all_line_words = re.findall(pattern, line)
        for word in all_line_words:
            word_lower = word.lower()
            if word_lower in result:
                result[word_lower] += 1

with open('./output.txt', 'w') as words_file:
    sorted_result = sorted(result.items(), key=lambda x: -x[1])
    for key, value in sorted_result:
        words_file.write(f"{key} - {value}\n")