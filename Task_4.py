import re

def identify_sentences(text):
    sentence_pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<!\b\w\.)(?<!["\'(])(?<=\.|\?|\!|\;|\n)\s+(?=[A-Z])'

    sentences = re.split(sentence_pattern, text)

    output_file = open('output_task4.txt', 'w', encoding='utf-8')
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
    
    total_tokens = len(tokens)
    unique_tokens = len(set(tokens))
    
    if total_tokens > 0:
        ttr = unique_tokens / total_tokens
    else:
        ttr = 0
    
    output_file.write(f'Type-Token Ratio = {unique_tokens}/{total_tokens} = {ttr:.2f}\n\n')

file_path = 'pg36034.txt'
file = open(file_path, 'r', encoding='utf-8')
text = file.read()
file.close()

identify_sentences(text)

corpus_tokens = re.findall(r'\b\w+\b|\S', text.lower())
total_corpus_tokens = len(corpus_tokens)
unique_corpus_tokens = len(set(corpus_tokens))
if total_corpus_tokens > 0:
    corpus_ttr = unique_corpus_tokens / total_corpus_tokens
else:
    corpus_ttr = 0

output_file = open('output_task4.txt', 'a', encoding='utf-8')
output_file.write(f'Type-Token Ratio for the whole corpus: {unique_corpus_tokens}/{total_corpus_tokens} = {corpus_ttr:.2f}\n')
output_file.close()