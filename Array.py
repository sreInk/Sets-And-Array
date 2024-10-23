import array as arr

an = arr.array('i',[1,3,5,3,5,6,9,5,1])
print("Orginal Array" +str(an))

print("How many Times 3 came" + str(an.count(3)))

an.reverse()
print("Uno Reverse")
print(str(an))
