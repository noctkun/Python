l=[21,42,53,35,46,4664,32,4,0,5,9,0,67,0,76,0,0]
count=0
for i in l:
    if i == 0:
        count+=1
        l.remove(i)
for j in range(count):
    l.append(0)
print(l)