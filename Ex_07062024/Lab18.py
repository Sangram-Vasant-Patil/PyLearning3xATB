#inbuilt functions
#Function --> Repeat the tasks - you can use function
#print(), input(), type(), format(), min, max, id(), sum(), avg()

#STRINGS
name = ("Sangram")
print(name)
print(type(name))
#id will show memory address where the variable is stored
print(id(name))
print(len(name))
#change text to upper cases
print(name.upper())
#change text to lower cases
print(name.lower())
#count
a = name.count("a") #-->counts a's in name sangram
print(a)
#find value in index
print(name[3])

#Python is immutable
name[0] = "A"
print(name)