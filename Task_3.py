import re
from collections import Counter

def frequency_analysis(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_freq = Counter(words)

    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    output_file = open('output_task3.txt', 'w', encoding='utf-8')
    for word, freq in sorted_word_freq:
        output_file.write(f'{freq} {word}\n')
    output_file.close()

file_path = 'pg36034.txt'
file = open(file_path, 'r', encoding='utf-8')
text = file.read()
file.close()

frequency_analysis(text)
