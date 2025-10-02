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






