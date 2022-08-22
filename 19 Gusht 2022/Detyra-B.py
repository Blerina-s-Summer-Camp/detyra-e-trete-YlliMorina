
list1 = [0.0, 50, 616, 12.5]
list2 = [10.10, 50, 61, 0.5, 108, 15.5]
list3 = [0.90, 50, 266, 1.0, 11, 10.5]
list4 = [1.9, 0.20, 50, 6601, 11.5]
list5 = [1.99, 0.05, 50, 7.2, 401, 16.5]

# Udhëzim: Për të gjetur vlerën mesatare të numrave minimal të fituar nga secila listë, 
# shfrytëzoni rreshtin 'array'
array = [list1, list2, list3, list4, list5]
#print(min(array))

shuma = (min(list1) + min(list2)+min(list3) + min(list4) + min(list5))
mesatarja = shuma/5

print(mesatarja)



