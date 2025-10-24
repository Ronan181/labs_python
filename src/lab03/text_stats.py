# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# # from ..my_lib.text import normalize, tokenize, count_freq, top_n
# # print(normalize("ПрИвЕт\nМИр\t"))
# # sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'mylib'))
# # current_dir = os.path.dirname(os.path.abspath(__file__))
# # lib_path = os.path.join(current_dir, '..', 'lib')
# # sys.path.insert(0, lib_path)

# from lib.text import normalize, tokenize, count_freq, top_n


# def phrase():
#     fraza=sys.stdin.read().strip()
#     if not fraza:
#         raise ValueError
    
#     normalize_fraza=normalize(fraza)
#     tokens=tokenize(normalize_fraza)
#     freq_count=count_freq(tokens)
#     most_usable_words=top_n(freq_count,5)
#     total_words=len(tokens)
#     unique_words=len(freq_count)
#     print(f'Всего слов:{total_words}')
#     print(f'Уникальных слов:{unique_words}')
#     print('Топ-5:')
#     for words,counts in most_usable_words:
#         print(f'{words}:{counts}')

# if __name__ == '__main__':
#     phrase()
