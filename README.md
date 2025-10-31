<h1>Программирование и алгоритмизация(Лабораторные работы)</h1>

<h1>Лабораторная работа №4</h1>

<h3>Задание №1:</h3>

```python
from pathlib import*
import csv
from typing import Iterable, Sequence
import sys
import os

sys.path.append('/Users/ars/Documents/GitHub/labs_python/src/lib/')
from text import *

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError
    try:
        text=path.read_text(encoding=encoding)
        text=normalize(text)
        return text
    except UnicodeDecodeError as a:
        raise UnicodeDecodeError() from a

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    if rows:
        for row in rows:
            if len(row)!=len(rows[0]):
                raise ValueError
    if header and rows and len(header)!=len(rows[0]):
        raise ValueError
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
            
write_csv([("word","count"),("test",3)], "data/check.csv")  
txt = read_text("data/input.txt") 
print(txt)
```
![input.png](images/lab04/input.png)
![exe1.png](images/lab04/exe11.png)
![check.png](images/lab04/check.png)

<h3>Задание №2:</h3>

```python
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
```
![input.png](images/lab04/input.png)
![exe1.png](images/lab04/exe1.png)
![report.png](images/lab04/report.png)

<h1>Лабораторная работа №3</h1>

<h3>Задание №1:</h3>

```python
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if yo2e:
        text=text.replace('ё', 'е').replace('Ё', 'Е')
    text=re.sub(r'\s', ' ', text)
    text=re.sub(r' +', ' ', text).strip()
    if casefold:
        text=text.casefold()
    return text
    
def tokenize(text: str) -> list[str]:
    pattern=r'[\w]+(?:-[\w]+)*'
    tokens=re.findall(pattern, text)
    return tokens

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq_dict={}
    for token in tokens:
        if token in freq_dict:
            freq_dict[token] += 1
        else:
            freq_dict[token] = 1
    return freq_dict

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
```
![exe1.png](images/lab03/exe1.png)

<h3>Задание №2:</h3>

```python
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
```
![exe2.png](images/lab03/exe2.png)


<h1>Лабораторная работа №2</h1>

<h3>Задание №1:</h3>

```python
def min_max(maxx_minn):
    if len(maxx_minn)!=0:
        return tuple([min(maxx_minn), max(maxx_minn)])
    else:
        raise ValueError
print('min_max')
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))

print(min_max([1.5, 2, 2.0, -3.1]))
 
def unique_sorted(el):
    el=list(set(el))
    el=sorted(el)
    return el
print('unique_sorted')
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

def flatten(flatten_el):
    result_flatten=[]
    for i in range(len(flatten_el)):
        if type(flatten_el[i]) in [list,tuple]:
            result_flatten+=flatten_el[i]
        else:
            raise TypeError
    return result_flatten
print('flatten')
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
```

![exe2.1.png](images/lab02/exe1.png)

![exe2.1(er).png](images/lab02/exe1(er).png)

<h3>Задание №2:</h3>

```python
def transpose(matrix):
    if not matrix:
        return []
    
    for el_mat in matrix:
        if len(el_mat)!=len(matrix[0]):
            raise ValueError
        
    result=[]
    for i in range(len(matrix[0])):
        transposes=[]
        for j in range(len(matrix)):
            transposes.append(matrix[j][i])
        result.append(transposes)
    return result
print('transpose')
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))


def row_sums(sum_matrix):
    if not sum_matrix:
        return []
    
    for el_mat in sum_matrix:
        if len(el_mat)!=len(sum_matrix[0]):
            raise ValueError
    
    summa=[]
    for el_mat in sum_matrix:
        el_sum = sum(el_mat)
        summa.append(el_sum)
    return summa
print('row_sums')
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[0, 0], [0, 0]]))


def col_sums(col_matrix):
    if not col_matrix:
        return []
    
    for el_mat in col_matrix:
        if len(el_mat)!=len(col_matrix[0]):
            raise ValueError
    result=[]
    for i in range(len(col_matrix[0])):
        summ=0
        for j in range(len(col_matrix)):
            summ+=col_matrix[j][i]
        result.append(summ)
    return result
print('col_sums')
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```

![exe2.2.png](images/lab02/exe2.png)

![exe2.2(er).png](images/lab02/exe2(er).png)

<h3>Задание №3:</h3>

```python
def format(tuple_inf):
    if len(tuple_inf)!=3:
        raise TypeError
    if type(tuple_inf[2])!=float:
        raise TypeError
    if type(tuple_inf[0])!=str:
        raise TypeError
    if type(tuple_inf[1])!=str:
        raise TypeError
    fio=tuple_inf[0].strip().split()
    gruppa=tuple_inf[1].strip()
    gpa=tuple_inf[2]
    fio_out=fio[0].capitalize()+' '
    if not fio:
        raise ValueError
    if not gruppa:
        raise ValueError
    if gpa<0:
        raise ValueError
    for i in range(1,len(fio)):
        fio_out+=fio[i][0].upper()+'.'
    print(fio_out+','+ f' гр. {tuple_inf[1]}',f'GPA {tuple_inf[2]:.2f}')
format(('Иванов Иван Иванович','BIVT-25',4.6))
format(("Петров Пётр", "IKBO-12", 5.0))
format(("Петров Пётр Петрович", "IKBO-12", 5.0))
format(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))
```

![exe2.3.png](images/lab02/exe3.png)

<h2>Лабораторная №1:</h2>

<h3>Задание №1:</h3>

```python
name=input()
vozrast=int(input())
vozrast_1=vozrast+1
print('Имя:',name)
print('Возраст:',vozrast)
print(f'Привет, {name}!',f'Через год тебе будет {vozrast_1}.')
```

![exe1.png](images/lab01/exe1.png)

<h3>Задание №2:</h3>

```python
a=input('a: ')
b=input('b: ')
a=float(a.replace(',','.'))
b=float(b.replace(',','.'))
sum=a+b
avg=(a+b)/2
print(f'sum={sum:.2f};',f'avg={avg:.2f}')
```
![exe2.png](images/lab01/exe2.png)


<h3>Задание №3:</h3>

```python
price=float(input())
discount=float(input())
vat=float(input())

base=price*(1 - discount/100)
vat_amount=base * (vat/100)
total=base+vat_amount
print('База после скидки:',  base,'₽')
print('НДС:',  vat_amount,'₽')
print('Итого к оплате:',  total,'₽')
```
![exe3.png](images/lab01/exe3.png)

<h3>Задание №4:</h3>

```python
m=int(input())
print('Минуты:',m)
print(f'{(m//60):02d}:{(m%60):02d}')
```
![exe4.png](images/lab01/exe4.png)

<h3>Задание №5:</h3>

```python
f,i,o=(input().split())
s=str(f)+str(i)+str(o)
print('ФИО:',f,i,o)
print(f'Инициалы: {f[0]+i[0]+o[0]}.')
print('Длина (символов):',len(s)+2)
```
![exe5.png](images/lab01/exe5.png)

<h3>Задание №6:</h3>

```python
ochnoe_obychenie=0
zaochnoe_obychenie=0

for n in range(int(input())):
    data=input().split()
    format=data[-1]

    if format=='True':
        ochnoe_obychenie+=1

    if format=='False':
        zaochnoe_obychenie+=1

print('out:', ochnoe_obychenie, zaochnoe_obychenie)
```
![exe6.png](images/lab01/exe6.png)

<h3>Задание №7:</h3>

```python
s=input('in: ')
for i in range(len(s)):
    if s[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        first_mem=i
        break

for i in range(len(s)):
    if s[i] in '0123456789' and s[i+1] not in '0123456789':
        second_mem=i+1
        break

last_mem=s.find('.')

distance = second_mem - first_mem
stroka=[]
for i in range(first_mem,last_mem+1,distance):
    stroka.append(s[i])
print('out:',''.join(stroka))
```
![exe7.png](images/lab01/exe7.png)
























































