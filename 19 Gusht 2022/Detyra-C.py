
list1 = ['Probit', 0.0, 'Academy', 616, 12.5]
list2 = ['Python', 0.5, 'Language', 1008, 15.5]
list3 = ['Computer', 1.0, 'Architecture', 1011, 10.5]
list4 = ['JavaScript', 1.9,'Language', 601, 11.5]
list5 = ['jQuery', 7.2, 'Language', 4301, 16.5]

#array = [list1, list2, list3, list4, list5]

numer1 = list1[-2]

array = [list1[-2], list2[-2], list3[-2], list4[-2], list5[-2]]
print(array)

#Shuma permes indeksimit negativ

shuma = array[-1] + array[-2] + array[-3] + array[-4] + array[-5]
average = shuma/5

print(average)

#for loop
shuma = 0
mesatarja = 0
for i in array:
    shuma += i
    mesatarja = shuma/5

print(mesatarja)

