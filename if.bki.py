#Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayan python uygulamasını yapınız.

#Formül: (Kilo / boy uzunluğunun karesi)
#0-18.4 => Zayıf

#18.5-24.9 => Normal

#25.0-29.9 => Fazla Kilolu

#30.0-34.9 => Şişman (Obez)
name = input('ad: ')
weight = float(input('kilo : '))
length = float(input('boy : '))
index= weight / length **2
if (index >= 0) and (index <= 18.4 ):
    print(f'{name} kilo indeksiniz {index} zayıf olan aralıktasınız ')
elif (index>18.4) and (index<=24.9):
    print(f'{name} kilo indeksiniz {index} normal olan aralıktasınız')
elif(index >= 25.0) and ( index <= 29.9):
    print(f'{name} kilo indeksiniz {index} fazla kilolu olan aralıktasınız')
elif(index >= 30.0) and ( index <= 34.9): 
     print(f'{name} kilo indeksiniz {index} obez olan aralıktasınız')
else:
     print('bilgileriniz yanlış.')