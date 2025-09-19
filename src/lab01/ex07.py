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


