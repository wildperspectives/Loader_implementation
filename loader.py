tokens=[[] for x in range(4)]

with open('objectCode.txt') as code:
    text = code.readlines()
    pos=0
    for lines in text:
        tokens[pos]=lines.split('^')
        pos+=1
 


print('The name of the object code : '+tokens[0][1])

for lines in tokens[1:]:
    if lines[0]=='E':
        break;

    counter=int(lines[1])

    for elems in lines[3:]:
        print(counter,elems[0:2])
        counter+=1
        print(counter,elems[2:4])
        counter+=1
        print(counter,elems[4:])