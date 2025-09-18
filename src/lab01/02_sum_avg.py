a=input('a: ')
b=input('b: ')
a=float(a.replace(',','.'))
b=float(b.replace(',','.'))
sum=a+b
avg=(a+b)/2
print(f'sum={sum:.2f};',f'avg={avg:.2f}')