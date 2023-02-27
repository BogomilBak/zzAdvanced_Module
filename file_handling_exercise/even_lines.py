symbols = ["-", ",", ".", "!", "?"]
result_line = []
with open('./text.txt', 'r') as words_file:
    split_words = words_file.read().split("\n")
    for line in range(0, len(split_words), 2):
        result = ''
        for word in reversed(split_words[line].split()):
            current_word = word
            for symbol in symbols:
                if symbol in current_word:
                    current_word = current_word.replace(symbol, "@")
                    print(current_word)
            result += current_word + ' '
        result_line.append(result)

with open('./output.txt', 'w') as result_file:
    for line in result_line:
        print(line)
        result_file.write(f"{line} \n")