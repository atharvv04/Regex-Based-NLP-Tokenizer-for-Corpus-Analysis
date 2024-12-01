import re

def identify_sentences(text):
    sentence_pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<!\b\w\.)(?<!["\'(])(?<=\.|\?|\!|\;|\n)\s+(?=[A-Z])'

    sentences = re.split(sentence_pattern, text)

    output_file = open('output_task1.txt', 'w', encoding='utf-8')
    for i, sentence in enumerate(sentences, start=1):
        if sentence.strip():
            output_file.write(f'<Sent id="{i}">\nText = {sentence.strip()}\n</Sent>\n')
    output_file.close()

file_path = 'pg36034.txt'
file = open(file_path, 'r', encoding='utf-8')
text = file.read()
file.close()

identify_sentences(text)
