markalar = ["honda","opel","audi"]

index = 0
for i in markalar:
    print(f"{index+1}-{markalar[index]}")
    index +=1


index = 0
for i in markalar:
       index +=1 
       print(f"{index}-{i}")


# enumerate
#-> üst tarafta yaptığımız indexleme ve yazdırma işini enumerate komutuyla yapabiliriz 
# enumerate kendisi listedeki elemanları indexliyerek list komutuyla yazdırır
x = enumerate(markalar)

print(list(x))

# for döngüsüyle enumerate kullanımı 
for i in enumerate(markalar):
    print(i)


#-> enumerate komutuyla zaten listedeki her bir elemanı indexliyoruz index ve value komutuyla direkt yazdırabiliriz.

for index,value in enumerate(markalar):
    print(index,value)


# f stringle böyle yazdırabiliriz.
for index,value in enumerate(markalar):
    print(f"{index+1}-{value}")    


# 10 dan başlatıp indexleyebiliriz.
for index,value in enumerate(markalar,10):
    print(f"{index}-{value}")
    



#zip

liste1 = [1,2,3,4,5]
liste2 = ["a","b","c","d","e"]
liste3 = [100,200,300,400,500]

print(list(zip(liste1,liste2,liste3)))
#-> zip komutuyla 3 farklı listeyi indexlerine göre birleştirebiliriz.

#for döngüsüyle zip metodunu kullanarak indexlerine göre listeleyebiliriz.
for i in zip(liste1,liste2,liste3):
    print(i)

#yukardaki döngünün çıktısı bu şekilde oluyor
#(1, 'a', 100)
#(2, 'b', 200)
#(3, 'c', 300)
#(4, 'd', 400)
#(5, 'e', 500)