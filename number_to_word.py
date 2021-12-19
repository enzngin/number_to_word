kat = { 0: "", 1: "Bin", 2: "Milyon",3: "Milyar"  }
birler = {0:"", 1:"Bir", 2:"İki", 3:"Üç",4:"Dört",5:"Beş",6:"Altı",7:"Yedi",8:"Sekiz",9:"Dokuz" }
onlar = { 0:"", 1:"On", 2:"Yirmi", 3:"Otuz",4:"Kırk",5:"Elli",6:"Altmış",7:"Yetmiş",8:"Seksen",9:"Doksan" }
yüzler = { 0:"", 1:"Yüz", 2:"İkiyüz", 3:"Üçyüz",4:"Dörtyüz",5:"Beşyüz",6:"Altıyüz",7:"Yediyüz",8:"Sekizyüz",9:"Dokuzyüz" }

def fillZero(number):
    number = str(number)
    if(len(number) % 3 == 1): #Başta 2 boşluk varsa (__1.456)
        return number.zfill(2 + len(number))
    elif(len(number) % 3 == 2): #Başta 1 boşluk varsa (_24.732)
        return number.zfill(1 + len(number))
    else:
        return number

def numberToWord (number): #Üç basamaklı bir sayının okunuşunu döndürür 345 -> ÜçyüzKırkBeş
    list = []
    num = fillZero(number)
    for i in range(len(num)):
        if i == 0:
            list.append(yüzler[int(num[0])])
        if i == 1:
            list.append(onlar[int(num[1])])
        if i == 2:
            list.append(birler[int(num[2])])
    word = "".join(list)
    return word

def numberParse(number): #Girilen sayıyı 3lü parçalara ayırır. Listeye atar liste döndürür
    number = fillZero(number)
    list = []
    varj = 0
    vari = 3
    for i in range(int(len(number) / 3)):
        list.append(number[varj:vari])
        varj += 3
        vari += 3
    list.reverse()
    return list

def returnFinalWord(number): #Üçlü parçalara ayrılıp liste haline getirilen sayıyı başına ölçek(bin,milyon,milyar) ekleyerek yazdırır
    if number < 1000:
        return numberToWord(number)
    else:
        list =[]
        number = numberParse(number)
        for i in range(len(number)-1, -1,-1):
            if number[1] == "001": # binler kısmı 001 olunca birBin tarzı bir okunuşu engeller
                if (i == 1):
                    list.append(kat[i])
                else:
                    list.append(numberToWord(number[i]) + kat[i])
            else:
                list.append(numberToWord(number[i]) + kat[i])
        word = " ".join(list)
        return word

x = int(input("Okunuşunu görmek istediğiniz sayıyı girin: "))
print(returnFinalWord(x))

