print ('Merhaba, Django Girls!')
if 3>2:
    print('calisiyor')
if 5>2 :
    print("5 gercekten de 2'den buyuktur")
else:
    print("5 2'den buyuk degildir")

name = "Zeynep"
if name == "Ayse":
    print("Selam Ayse!")
elif name == "Zeynep":
    print("Selam Zeynep!")
else:
    print("Selam yabanci")
volume = 57
if volume <20:
    print("cok sessiz.")
elif 20 <= volume < 40:
    print ("guzel bir fon muzigi")
elif 40 <= volume < 60:
    print("Harika her notayi duyabiliyorum")
elif 60 <= volume < 80 :
    print ("Parti baslasin")
elif 80 <= volume <100 :
    print ("Biraz gurultulu")
else:
    print("kulaklarim agriyor! :(")

if volume < 20 or volume > 80:
    volume = 50
    print("That's better!")

def hi():
    print('Merhaba!')
    print('Nasilsin?')
hi()

def hi(name):
    if name=="Ayse":
        print ("Merhaba Ayse!")
    elif name == "Zeynep":
        print ("Merhaba Zeynep!")
    else:
        print ("Merhaba Yabanci!")
hi(name)
hi("Ayse")
hi("Zeynep")

def hi(name):
    print ("Merhaba " + name + "!")
hi ("Seda")

kizlar= ["Seda", "Gul", "Pinar", "Ayse", "Esra"]
for name in kizlar:
    def hi(name):
        print("Merhaba" + name + "!")
kizlar= ["Seda", "Gul", "Pinar", "Ayse", "Esra"]
for name in kizlar:
    hi(name)
    print ('Siradaki kiz')

for i in range (1,6):
    print(i)
    
