print("Hello")
slowo = "informatyka"
print(slowo[-1])
print(slowo[-5:])
print(slowo[:5])
print(slowo[2::2])
print(slowo[-1:-8:-2])
print("Podaj slowo")
slowo = input()
if slowo == slowo[::-1]:
    print(slowo, "jest palindromem")
else:
    print(slowo, "nie jest palindromem")
suma = 0
for i in range(10, 100, 2):
    print(i,end=", ")
    suma=suma+i
print("suma wynosi",suma)
print("podaj pierwszą liczbę")
a=int(input())
print("Podaj drugą liczbę")
b=int(input())
while b!=0:
    a,b=b,a%b
print("nwd",a)
print("podaj liczbę")
liczba = int(input())
pierwsza= True
for i in range(2, liczba):
    if liczba%i==0:
        pierwsza = False
        print("Liczba nie jest pierwsza")
        break
if pierwsza:
    print("liczba pierwsza")

czy_pierwsza = [1 for x in range(liczba)]
czy_pierwsza[0]=0
czy_pierwsza[1]=0
print(czy_pierwsza)
pierwiastek = int(len(czy_pierwsza)**0.5)+1
for indeks in range(pierwiastek+1):
    if czy_pierwsza[indeks]==1:
        for i in range(indeks*2, len(czy_pierwsza), indeks):
            czy_pierwsza[i] = 0
pierwsze = []
for i in range(len(czy_pierwsza)):
    if(czy_pierwsza[i] == 1):
        pierwsze.append(i)
print(pierwsze)
print("podaj następną liczbę")
liczba = int(input())
czynniki = []
czynnik = 2
while liczba > 1:
    if liczba % czynnik == 0:
        czynniki.append(czynnik)
        liczba = liczba // czynnik
    else:
        czynnik = czynnik + 1
print(czynniki)