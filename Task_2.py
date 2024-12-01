import re

def identify_sentences(text):
    sentence_pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<!\b\w\.)(?<!["\'(])(?<=\.|\?|\!|\;|\n)\s+(?=[A-Z])'

    sentences = re.split(sentence_pattern, text)

    output_file = open('output_task2.txt', 'w', encoding='utf-8')
    for i, sentence in enumerate(sentences, start=1):
        if sentence.strip():
            output_file.write(f'<Sent id="{i}">\nText = {sentence.strip()}\n')
            identify_words(sentence, i, output_file)
            output_file.write('</Sent>\n')
    output_file.close()

def identify_words(sentence, sentence_id, output_file):
    tokens = re.findall(r"[\w']+|[.,!?;]", sentence)

    for j, token in enumerate(tokens, start=1):
        output_file.write(f'Token {j} = {token}\n')

file_path = 'pg36034.txt'
file = open(file_path, 'r', encoding='utf-8')
text = file.read()
file.close()

identify_sentences(text)
