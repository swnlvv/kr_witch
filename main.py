##ПОМЕНЯТЬ НА НЕОБХОДИМУЮ ДИРЕКТОРИЮ

##import os
##os.chdir("c:\\Users\\Лия\\Documents\\it\\pythonuni\\kr\\witch")
## считывание инпута

with open("input1.txt", "r") as file:
    lines = file.readlines()


witch=[]
i=0
for line in lines:
    ## создание пустой строки в листе для последующего ее заполнения
    witch.append("")
   
    ## удаление разделителей строк
    s=list(line.rstrip("\n"))
    
    ## удаление каждого четвертого символа
    del s[3::4]

    ## заполнение листа
    witch[i]=(''.join(s))
    i+=1

## перевод в сет и обратно для удаления повторений
witch=list(set(witch))

## сорт листа
witch.sort()

with open("output.txt", "w") as file:
    for item in witch:
        file.write("%s\n" % item)