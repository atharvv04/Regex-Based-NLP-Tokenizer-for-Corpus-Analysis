# README

This repository contains Python scripts to perform various text processing tasks on a corpus. Below are the details of each task performed along with additional information and assumptions made during the process.

## Details
- The corpus file `pg36034.txt` is assumed to be in the same directory as the Python files.

## Assumptions and Details for Task 1: Identifying Sentences
- A sentence is denoted by a group of words followed by a punctuation (full stop, question mark, exclamation mark) or a whitespace.
  - The punctuation must be followed by a capital letter, number, or newline character for it to qualify as a sentence.
  - "1.F." (for example) will be considered as a separated sentence since it acts as a heading.
  - "1.F.1." (for example) will not be considered as a separate sentence since it is part of the paragraph.
  - "... " will be considered as a sentence break.
  - Bullet points are not considered as sentence breaks.
  - Newline characters in the text will not be modified to ignore newline.
    Example: Text = Volunteers and financial support to provide volunteers with the\n
    assistance they need are critical to reaching Project Gutenberg™’s\n
    goals and ensuring that the Project Gutenberg™ collection will\n
    remain freely available for generations to come. 
  - Quotation marks will not be exempt from sentence breaks.
    Example: "What is it? Give over, do you hear, you stupid woman?"
    Sentence 1 = "What is it?
    Sentence 2 = Give over, do you hear, you stupid woman?

## Assumptions and Details for Task 2: Identifying Words
- Punctuation marks will be considered as individual tokens.

## Assumptions and Details for Task 3: Frequency Analysis
- The list of frequencies will be printed in descending order.

## Assumptions and Details for Task 4: Type-Token Ratio
- Tokenization is done in the same manner as in Task 2.
- The full stop will be considered as an individual token for calculating the type-token ratio.
