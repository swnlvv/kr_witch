##поменять на необходимую директорию

##import os
##os.chdir("c:\\Users\\Лия\\Documents\\it\\pythonuni\\kr\\witch")
## считывание инпута

with open("input1.txt", "r") as file:
    lines = file.readlines()

## создание листа из строк из инпута
witch=[]
for line in lines:
    witch.append(line)

## удаление строковых разделителей
witch=[line.rstrip() for line in witch]
## перевод в сет и обратно для удаления повторений, подсчет длины сета
witch=list(set(witch))
l=len(set(witch))
## сорт инпута
witch.sort()
##срез каждого четвертого символа
i=0
while i<l:

    s=list(witch[i])
    del s[3::4]
    witch[i]=(''.join(s))
    i+=1
##вывод данных
with open("output.txt", "w") as file:
    for item in witch:
        file.write("%s\n" % item)
