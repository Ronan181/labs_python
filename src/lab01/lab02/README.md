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

![exe1.png](images/lab02/exe1.png)

