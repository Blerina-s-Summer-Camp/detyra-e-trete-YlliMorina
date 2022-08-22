#Kushtet
varg = [10,32,2,55,-11]

#Shembull i deklarimit te x-it dhe nje shembull i for loops me conditional statements
for x in varg:
    if x<0:
      print("X-është numer negativ")
    elif x==0:
        print("X-është zero")
    else :
        print("X-është numer pozitiv")

#def - eshte funksion per metodat

#forma e metodes kur inicializohen variablat jashte metodes
# funksioni per gjetjen e mesatares
a=5.2 
b=2.3
c=9.5
def metoda():
  return (a+b+c)/3

print(metoda())

#forma e metodes kur inicializohen variablat brenda metodes
def metoda(a,b,c):
  return (a+b+c)/3

print(metoda(2,10,5))

