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

