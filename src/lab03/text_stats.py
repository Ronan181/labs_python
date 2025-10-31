import sys
import os

sys.path.append('/Users/ars/Documents/GitHub/labs_python/src/lib/')
from text import *

def phrase():
    fraza=sys.stdin.readline().strip()
    if not fraza:
        print('Ввода нет')
    
    normalize_fraza=normalize(fraza)
    tokens=tokenize(normalize_fraza)
    freq_count=count_freq(tokens)
    most_usable_words=top_n(freq_count,5)
    total_words=len(tokens)
    unique_words=len(freq_count)

    print(f'Всего слов:{total_words}')
    print(f'Уникальных слов:{unique_words}')
    print('Топ-5:')
    for words,counts in most_usable_words:
        print(f'{words}:{counts}')
    
phrase()


