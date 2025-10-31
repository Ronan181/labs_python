import sys
import os
import csv
from collections import Counter

sys.path.append('/Users/ars/Documents/GitHub/labs_python/src/lib/')
from text import *

def main():
    input_file="data/input.txt"
    output_file="data/report.csv"
    encoding="utf-8"
    with open(input_file, 'r', encoding=encoding) as f:
        text=f.read()
    text=normalize(text)
    words=tokenize(text)
    word_count=Counter(words)
    sorted_words=sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("word,count\n")
        for word, count in sorted_words:
            f.write(f"{word},{count}\n")
    print(f"Всего слов: {len(words)}")
    print(f"Уникальных слов: {len(word_count)}")
    print("Топ-5:")
    for word, count in sorted_words[:5]:
        print(f"{word}:{count}")
main()


