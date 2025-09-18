<h1>Программирование и алгоритмизация(Лабораторные работы)</h1>

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



















